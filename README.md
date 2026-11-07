# Resume Intelligence AI

An AI-powered resume evaluator built for **Internee.pk Generative AI Internship — Assignment #2**.

## Features
- Upload PDF or DOCX resumes (8 MB maximum).
- Extract resume text with pypdf and python-docx.
- Evaluate against a target role and experience level.
- Generate a 0–100 quality score, strengths, prioritized improvements, skill evidence, ATS feedback, an action plan, and honest bullet rewrites.
- Keep the OpenAI API key on the server; resume contents are processed in memory and are not saved by this app.

## Tech stack
Python, Flask, OpenAI Responses API, pypdf, python-docx, HTML, CSS, JavaScript, and Vercel.

## Local setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

Set your API key as an environment variable (never commit it):
```bash
# macOS/Linux
export OPENAI_API_KEY="your-key"
# PowerShell
$env:OPENAI_API_KEY="your-key"
```

Run:
```bash
python api/index.py
```
Open http://127.0.0.1:5000.

## Vercel deployment
1. Import this repository into Vercel.
2. Set `OPENAI_API_KEY` in Project Settings → Environment Variables for Production (and Preview if needed).
3. Redeploy after changing environment variables.
4. Optional: set `OPENAI_MODEL`; default is `gpt-4.1-mini`.

## API
- `GET /api/health` — service health check.
- `POST /api/analyze` — multipart form with `resume` (PDF/DOCX), optional `target_role`, `experience_level`, and `focus`.

## Limitations and responsible use
- Scanned/image-only PDFs require OCR and are not supported yet.
- AI feedback can be incomplete or incorrect; verify every recommendation.
- The evaluator must not be used as a hiring decision or a prediction of employability.
- It is designed to avoid inventing qualifications or metrics; users should verify all suggested rewrites.
- For public production use, add rate limiting, malware scanning, abuse monitoring, and an appropriate privacy notice.

## Live demo

Production app: https://resume-intelligence-ai-eta.vercel.app

The interface is deployed on Vercel. To enable live AI analysis, configure a valid `OPENAI_API_KEY` in the Vercel Production environment and redeploy. The application intentionally returns HTTP 503 when this server-side secret is missing; never place the key in frontend code or commit it to Git.
