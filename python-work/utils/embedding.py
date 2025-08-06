# utils/embedding_utils.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingUtils:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, texts):
        """
        Fit and transform text data into TF-IDF vectors.
        """
        return self.vectorizer.fit_transform(texts)

    def transform(self, new_texts):
        """
        Transform new text data using the existing TF-IDF model.
        """
        return self.vectorizer.transform(new_texts)

    @staticmethod
    def calculate_similarity(vector1, vector2):
        """
        Calculate cosine similarity between two vectors.
        """
        return cosine_similarity(vector1, vector2)

if __name__ == "__main__":
    texts = [
        "Python developer with experience in AWS and Docker",
        "Looking for backend developer skilled in Java and Spring Boot"
    ]
    emb = EmbeddingUtils()
    vecs = emb.fit_transform(texts)
    sim = emb.calculate_similarity(vecs[0:1], vecs[1:])
    print(f"Similarity Score: {sim[0][0]:.2f}")
