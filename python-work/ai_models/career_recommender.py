# ai_models/career_recommender.py
from difflib import get_close_matches

# Example career paths with required skills
CAREER_PATHS = {
    "Data Scientist": ["python", "machine learning", "tensorflow", "pandas", "numpy"],
    "Backend Developer": ["python", "flask", "django", "sql", "docker"],
    "Frontend Developer": ["javascript", "html", "css", "react"],
    "DevOps Engineer": ["aws", "docker", "kubernetes", "ci/cd"],
}

def recommend_career(skills: list):
    """
    Recommend career paths based on extracted skills.
    :param skills: list of detected skills
    :return: list of recommended careers
    """
    if not skills:
        return ["General Software Engineer"]  # fallback recommendation

    recommended = []
    for career, required_skills in CAREER_PATHS.items():
        matches = len(set(skills) & set(required_skills))
        if matches > 0:
            recommended.append({"career": career, "match_count": matches})

    # Sort by match count (descending)
    recommended.sort(key=lambda x: x["match_count"], reverse=True)

    return [r["career"] for r in recommended[:3]] or ["General Software Engineer"]

