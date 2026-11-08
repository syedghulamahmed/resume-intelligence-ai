# Resume Intelligence AI

A resume-review application for PDF and DOCX files. It evaluates the resume against a target role and provides evidence-based strengths, prioritized improvements, skills assessment, ATS-structure feedback, and suggested bullet rewrites.

## Features
- Upload PDF or DOCX resumes (8 MB maximum).
- Extract text with pypdf and python-docx.
- Remove common direct identifiers (name-like header, email, phone, ID number, address labels, and links) before the AI request.
- Generate a role-aware review, score, strengths, improvement priorities, and an action plan.
- Clearly labelled rules-based fallback when live AI is unavailable.

## Stack
Python, Flask, Vireonix Chat Completions API, pypdf, python-docx, HTML, CSS, JavaScript, Vercel.

## AI provider
The server sends the redacted resume text to Vireonix's OpenAI-compatible `/v1/chat/completions` endpoint with model `auto`. No API key or payment card is required. The public API has per-IP hourly limits and no SLA; temporary 429 or service errors trigger a transparent local baseline review.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python api/index.py
```
Open http://127.0.0.1:5000.

No provider API key is required.

## API
- `GET /api/health` — service/provider health.
- `POST /api/analyze` — multipart fields: `resume` (PDF/DOCX), optional `target_role`, `experience_level`, and `focus`.

## Privacy and responsible use
Before upload/analysis, the interface requires explicit consent and explains that prompts, outputs, and related chat traces sent to Vireonix may be retained and used for training and product improvement. It also links to https://vireonix.ai/terms. Common direct identifiers are redacted automatically, but redaction cannot guarantee removal of every identifying or sensitive detail. Users should not upload confidential, sensitive, or unauthorized information. The app processes the uploaded file in memory and does not intentionally persist it. AI scores are qualitative guidance, not ATS certification, hiring predictions, or employment decisions. Verify suggested edits and never accept fabricated metrics or credentials.

MIT License.
