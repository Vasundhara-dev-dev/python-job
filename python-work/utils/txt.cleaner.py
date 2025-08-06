# utils/text_cleaner.py
import re
import string
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """
    Cleans the input text by removing punctuation, stopwords, and extra spaces.
    """
    if not text:
        return ""
    
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]
    
    return " ".join(words)

if __name__ == "__main__":
    sample = "Experienced in Python, Machine Learning & AWS (3+ years)."
    print(clean_text(sample))
