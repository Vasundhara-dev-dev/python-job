# ai_models/job_matcher.py
# ai_models/job_matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example job database (you can later load from DB or CSV)
JOB_LISTINGS = [
    {"title": "Backend Developer", "description": "Develop APIs, work with Python, Flask, Django, SQL, Docker"},
    {"title": "Data Scientist", "description": "Work with machine learning, Python, TensorFlow, pandas, numpy"},
    {"title": "DevOps Engineer", "description": "AWS, Docker, Kubernetes, CI/CD pipelines, cloud deployment"},
    {"title": "Frontend Developer", "description": "React, JavaScript, HTML, CSS, UI/UX development"}
]

def match_jobs(resume_input, top_n=3):
    """
    Match resume text or parsed dict with job descriptions using TF-IDF + cosine similarity.
    :param resume_input: raw text or dict with 'raw_text'
    :param top_n: number of top job matches
    :return: list of top matching jobs with scores
    """
    resume_text = resume_input["raw_text"] if isinstance(resume_input, dict) else resume_input

    corpus = [resume_text] + [job["description"] for job in JOB_LISTINGS]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    ranked_jobs = sorted(zip(JOB_LISTINGS, cosine_similarities), key=lambda x: x[1], reverse=True)

    return [{"job": job["title"], "score": float(score)} for job, score in ranked_jobs[:top_n]]
