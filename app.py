import re
from collections import OrderedDict
import streamlit as st

st.set_page_config(page_title="AI Medical Note Summarizer", page_icon="🩺", layout="centered")

DISCLAIMER = (
    "Demo only — not for diagnosis, treatment, or clinical decision-making. "
    "Always require human review."
)

SYMPTOM_WORDS = [
    "pain", "fever", "cough", "nausea", "vomiting", "fatigue", "dizziness",
    "headache", "shortness of breath", "sob", "swelling", "anxiety", "chest pain",
    "rash", "diarrhea", "constipation", "weakness", "blurred vision"
]

MEDICATION_HINTS = [
    "mg", "tablet", "capsule", "daily", "twice daily", "prn", "ibuprofen",
    "acetaminophen", "metformin", "lisinopril", "amoxicillin", "aspirin"
]

TIMELINE_HINTS = [
    "today", "yesterday", "last week", "2 days", "3 days", "1 week", "2 weeks",
    "for months", "for years", "since", "started", "worsened", "improved"
]


def clean_sentences(text: str):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def first_matching_sentence(sentences, keywords):
    for s in sentences:
        lower = s.lower()
        if any(k in lower for k in keywords):
            return s
    return ""


def extract_symptoms(text: str):
    found = []
    lower = text.lower()
    for word in SYMPTOM_WORDS:
        if word in lower:
            found.append(word)
    return list(OrderedDict.fromkeys(found))


def extract_medications(sentences):
    meds = []
    for s in sentences:
        lower = s.lower()
        if any(hint in lower for hint in MEDICATION_HINTS):
            meds.append(s)
    return meds[:5]


def extract_timeline(sentences):
    clues = []
    for s in sentences:
        lower = s.lower()
        if any(hint in lower for hint in TIMELINE_HINTS):
            clues.append(s)
    return clues[:5]


def generate_followup_questions(symptoms, meds):
    questions = []
    if symptoms:
        questions.append(f"When did the {', '.join(symptoms[:3])} start, and has it changed over time?")
        questions.append("How severe are the symptoms, and what makes them better or worse?")
    else:
        questions.append("What is the main concern or symptom the patient wants addressed today?")

    if meds:
        questions.append("Are the listed medications current, and has the patient missed any recent doses?")
    else:
        questions.append("Is the patient currently taking any prescription, OTC, or herbal medications?")

    questions.append("Are there any recent test results, prior episodes, or relevant medical history to add?")
    return questions


def summarize_note(text: str):
    sentences = clean_sentences(text)
    chief_concern = first_matching_sentence(sentences, SYMPTOM_WORDS) or (sentences[0] if sentences else "")
    symptoms = extract_symptoms(text)
    meds = extract_medications(sentences)
    timeline = extract_timeline(sentences)
    followups = generate_followup_questions(symptoms, meds)

    return {
        "Chief Concern": chief_concern or "Not clearly identified",
        "Symptoms Mentioned": symptoms or ["None clearly identified"],
        "Medications Mentioned": meds or ["None clearly identified"],
        "Timeline Clues": timeline or ["No clear timeline clues found"],
        "Follow-up Questions": followups,
    }


def format_summary(summary):
    lines = []
    lines.append("AI MEDICAL NOTE SUMMARY (DEMO)")
    lines.append("Not for diagnosis or treatment. Human review required.")
    lines.append("")
    for key, value in summary.items():
        lines.append(f"{key}:")
        if isinstance(value, list):
            for item in value:
                lines.append(f"- {item}")
        else:
            lines.append(f"- {value}")
        lines.append("")
    return "\n".join(lines)


st.title("AI Medical Note Summarizer")
st.caption(DISCLAIMER)

default_text = """Patient reports fatigue and dizziness for the last week. Mild headache started yesterday.
Currently taking lisinopril 10 mg daily and ibuprofen as needed. Denies chest pain.
Symptoms worsen when standing quickly. History of high blood pressure."""

note = st.text_area("Paste a medical note below", value=default_text, height=220)

col1, col2 = st.columns(2)

with col1:
    run_clicked = st.button("Generate Summary", use_container_width=True)

with col2:
    clear_clicked = st.button("Clear Text", use_container_width=True)

if clear_clicked:
    st.experimental_rerun()

if run_clicked and note.strip():
    summary = summarize_note(note)
    st.subheader("Structured Summary")

    for section, value in summary.items():
        st.markdown(f"**{section}**")
        if isinstance(value, list):
            for item in value:
                st.write(f"- {item}")
        else:
            st.write(value)

    output = format_summary(summary)
    st.download_button(
        "Download Summary as TXT",
        data=output,
        file_name="medical_note_summary_demo.txt",
        mime="text/plain",
        use_container_width=True,
    )

st.markdown("---")
st.markdown(
    "**Portfolio Tip:** Upload this project to GitHub and describe it as a demo project showing "
    "healthcare AI workflow thinking, structured summarization, and responsible AI awareness."
)