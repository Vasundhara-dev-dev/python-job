# tests/test_endtoend_model.py

import os
import pytest
from ai_models.resume_parser import parse_resume
from ai_models.skills_extractor import extract_and_normalize
from ai_models.job_matcher import match_jobs
from ai_models.career_recommender import recommend_career
from ai_models.feedback_generator import generate_feedback
from ai_models.resume_quality_predictor import predict_resume_quality

@pytest.mark.parametrize("resume_text", [
    "Python developer with AWS, Docker, and Machine Learning experience.",
    "Frontend developer skilled in React, JavaScript, and CSS."
])
def test_full_pipeline_external_model(resume_text):
    # Simulate parsing
    parsed = {"raw_text": resume_text, "skills": extract_and_normalize(resume_text)}

    # Job Matching
    matches = match_jobs(parsed)

    # Career Recommendations
    recs = recommend_career(parsed["skills"])

    # Feedback (pass all required args)
    fb = generate_feedback(parsed["skills"], matches, recs)

    # Model Quality Prediction
    quality = predict_resume_quality(resume_text)

    # Assertions
    assert isinstance(parsed["skills"], list)
    assert len(fb) > 10
    assert isinstance(quality, str)
    print("\n--- FEEDBACK ---\n", fb)

