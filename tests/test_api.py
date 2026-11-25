from io import BytesIO

from docx import Document

import api.index as service


def make_docx(text: str) -> BytesIO:
    document = Document()
    for line in text.splitlines():
        document.add_paragraph(line)
    stream = BytesIO()
    document.save(stream)
    stream.seek(0)
    return stream


def test_health_endpoint_reports_service():
    response = service.app.test_client().get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["service"] == "resume-intelligence-ai"


def test_analyze_requires_resume():
    response = service.app.test_client().post("/api/analyze")
    assert response.status_code == 400
    assert "Upload a resume" in response.get_json()["error"]


def test_rejects_unsupported_file_type():
    response = service.app.test_client().post(
        "/api/analyze",
        data={"resume": (BytesIO(b"plain text"), "resume.txt")},
        content_type="multipart/form-data",
    )
    assert response.status_code == 400
    assert "PDF or DOCX" in response.get_json()["error"]


def test_rejects_invalid_pdf_signature():
    response = service.app.test_client().post(
        "/api/analyze",
        data={"resume": (BytesIO(b"not a pdf"), "resume.pdf")},
        content_type="multipart/form-data",
    )
    assert response.status_code == 400
    assert "valid PDF" in response.get_json()["error"]


def test_anonymization_removes_common_direct_identifiers():
    raw = (
        "John Smith\nSoftware Engineer\n"
        "john.smith@example.com\n"
        "+1 (415) 555-0199\n"
        "https://linkedin.com/in/johnsmith\n"
        "12345-1234567-1\n"
        "Experience\nBuilt an API."
    )
    result = service.anonymize_resume(raw)
    assert "john.smith@example.com" not in result
    assert "415" not in result
    assert "linkedin.com" not in result
    assert "12345-1234567-1" not in result
    assert "Built an API" in result


def test_provider_failure_returns_explicit_baseline_fallback(monkeypatch):
    def unavailable(_messages, timeout=28):
        raise RuntimeError("provider unavailable")

    monkeypatch.setattr(service, "call_blockrun", unavailable)
    resume = make_docx(
        "Jane Candidate\n"
        "Education\nBachelor of Computer Science\n"
        "Skills\nPython React SQL\n"
        "Projects\nBuilt a student portal using React and Python."
    )
    response = service.app.test_client().post(
        "/api/analyze",
        data={"resume": (resume, "resume.docx"), "target_role": "Software Intern"},
        content_type="multipart/form-data",
    )
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["source"] == "built-in"
    assert "not AI feedback" in payload["notice"]
    assert payload["analysis"]["overall_score"] >= 20
