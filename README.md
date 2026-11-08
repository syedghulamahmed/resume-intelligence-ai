# Resume Intelligence AI

A resume-review application for PDF and DOCX files. It evaluates a resume against a target role and provides evidence-based strengths, prioritized improvements, skills assessment, ATS-structure feedback, and suggested bullet rewrites.

## Features
- Upload PDF or DOCX resumes (8 MB maximum).
- Extract text with pypdf and python-docx.
- Remove common direct identifiers (name-like header, email, phone, ID number, address labels, and links) before model inference.
- Generate a role-aware review, score, strengths, improvement priorities, and an action plan.
- Clearly labelled rules-based fallback when live AI is unavailable.

## Stack
Python, Flask, BlockRun Chat Completions API, pypdf, python-docx, HTML, CSS, JavaScript, Vercel.

## AI provider
The server sends redacted resume text through BlockRun's OpenAI-compatible chat-completions endpoint using free model `nvidia/nemotron-3.5-bolt`, with `poolside/laguna-xs-2.1` as a fallback. No API key, wallet, payment card, or account is required. Free model capacity and IP rate limits may change; temporary provider errors trigger a transparent local baseline review.

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
Before analysis, the interface requires consent and explains that resume text (after common-identifier redaction) is sent through BlockRun to the selected model provider. BlockRun states it does not retain or train on prompts; upstream model-provider terms apply. Read [BlockRun Privacy](https://blockrun.ai/privacy) and [Terms](https://blockrun.ai/terms). Redaction is best-effort and cannot guarantee removal of every identifying or sensitive detail. Upload only information you are authorized to share; do not upload confidential or sensitive records. The app processes files in memory and does not intentionally persist them. Scores are qualitative guidance, not ATS certification, hiring predictions, or employment decisions. Verify suggested edits and never accept fabricated metrics or credentials.

MIT License.
