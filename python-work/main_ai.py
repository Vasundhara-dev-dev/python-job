# main_ai.py

import os
from ai_models.resume_parser import parse_resume
from ai_models.skills_extractor import extract_and_normalize
from ai_models.job_matcher import match_jobs
from ai_models.career_recommender import recommend_career
from ai_models.feedback_generator import generate_feedback

def analyze_resume(file_path: str):
    """Complete pipeline: parse → extract skills → match → recommend → feedback"""
    if not os.path.exists(file_path):
        return {"error": "File not found."}

    # Step 1: Parse resume text
    parsed_text = parse_resume(file_path)

    # Step 2: Extract skills
    skills = extract_and_normalize(parsed_text)

    # Step 3: Match jobs (from sample dataset or DB)
    matched_jobs = match_jobs(parsed_text)

    # Step 4: Career recommendations
    recommendations = recommend_career(skills)

    # Step 5: AI-powered feedback
    feedback = generate_feedback(skills, matched_jobs, recommendations)

    # Final output
    return {
        "parsed_text": parsed_text[:300] + "...",  # preview
        "skills": skills,
        "job_matches": matched_jobs,
        "career_recommendations": recommendations,
        "feedback": feedback
    }

if __name__ == "__main__":
    
    test_file = r"C:\Users\Khushboo\OneDrive\Desktop.pdf"  
    result = analyze_resume(test_file)
    print("🔍 Analysis Result:")
    for key, value in result.items():
        print(f"{key}: {value}\n")
