# ai_models/resume_quality_predictor.py

import os
import joblib

# Define paths to the cloned model files
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models/classifier1.pkl"))
VECTORIZER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models/vectorizer1.pkl"))

# Load model & vectorizer safely
model = None
vectorizer = None

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    print("[Warning] Pretrained model files not found. Model not loaded.")

def predict_resume_quality(resume_text: str) -> str:
    """
    Predict the resume category/quality using JeevikaaAnand's pretrained model.
    Returns a category label or error message if model is missing.
    """
    if model is None or vectorizer is None:
        return "Model not available"

    vec = vectorizer.transform([resume_text])
    prediction = model.predict(vec)
    return str(prediction[0])
