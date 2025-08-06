#
# ai_models/feedback_generator.py

def generate_feedback(skills, matched_jobs, recommended_careers):
    """
    Generate feedback based on extracted skills, job matches, and career recommendations.
    :param skills: list of detected skills
    :param matched_jobs: list of matched jobs (with scores)
    :param recommended_careers: list of career recommendations
    :return: feedback string
    """
    feedback = []

    # Skill Feedback
    if not skills:
        feedback.append("No skills detected. Consider adding technical keywords to your resume.")
    else:
        feedback.append(f"Detected skills: {', '.join(skills)}")

    # Job Match Feedback
    if matched_jobs:
        top_job = matched_jobs[0]['job']
        feedback.append(f"Your resume best matches the role: {top_job}")
    else:
        feedback.append("No strong job matches found. Try improving your resume keywords.")

    # Career Recommendations
    if recommended_careers:
        feedback.append(f"Suggested career paths: {', '.join(recommended_careers)}")
    else:
        feedback.append("Unable to provide career recommendations. Add more relevant skills.")

    return "\n".join(feedback)
