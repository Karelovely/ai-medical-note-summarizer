# AI Medical Note Summarizer (Demo)

A beginner-friendly demo project that turns a pasted medical note into a structured summary.

## Important
This is a portfolio/demo project only. It is **not** for diagnosis, treatment, or clinical decision-making.

## What this project does
- Accepts pasted medical note text
- Produces a structured summary with:
  - Chief concern
  - Symptoms
  - Medications mentioned
  - Timeline clues
  - Recommended follow-up questions
- Saves the summary to a text file if desired

## Why this is useful
Healthcare teams often work with long, unstructured notes. A summarization workflow can help organize information faster and more consistently.

## Skills this demonstrates
- Applied AI product thinking
- NLP / summarization concepts
- Python
- Streamlit
- Prompt-style structured extraction logic
- Responsible AI awareness

## Files
- `app.py` — Streamlit app
- `requirements.txt` — packages to install
- `sample_note.txt` — example input
- `.gitignore` — ignores Python cache files

## How to run
1. Install Python on your computer
2. Open terminal in this folder
3. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Suggested GitHub Repo Name
`ai-medical-note-summarizer`

## Suggested Resume Project Line
Built a demo AI medical note summarizer that converts unstructured notes into structured summaries and follow-up questions using Python and Streamlit.

## Interview Talking Point
I built this project to show how AI can support healthcare workflows by organizing long-form text into a faster, easier-to-review summary while keeping human review in the loop.