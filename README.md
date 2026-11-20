# AI Resume Analyzer (Beginner Version)

A small Flask app that compares words in a plain-text resume with skills mentioned in a job description.

## Features
- Upload a `.txt` resume.
- Paste a job description.
- See matched and missing skills.
- Get a simple keyword-match percentage.

## Run
1. Install Python 3.10+.
2. Open this folder in a terminal.
3. Run `python -m venv .venv`.
4. Activate it: Windows `.venv\\Scripts\\activate`; macOS/Linux `source .venv/bin/activate`.
5. Run `pip install -r requirements.txt`.
6. Run `python app.py` and open http://127.0.0.1:5000.

## Limitation
The percentage is a simple keyword match, not an actual ATS rating. Add your own skills and test files as you learn.
