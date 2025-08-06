# ai_models/skills_extractor.py
import re

# Sample skills list (you can expand this or load from dataset)
SKILL_SET = [
    "python", "java", "c++", "flask", "django", "aws", "docker", "machine learning",
    "tensorflow", "pytorch", "sql", "html", "css", "javascript"
]

def extract_and_normalize(text: str):
    """
    Extracts skills from resume text and normalizes them.
    Returns a list of matched skills.
    """
    if not isinstance(text, str):
        return []
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_SET:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(set(found_skills))
