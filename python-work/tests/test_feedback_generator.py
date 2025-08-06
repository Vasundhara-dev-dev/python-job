from ai_models.feedback_generator import generate_feedback

def test_feedback_generation():
    # Arrange
    sample_text = "Machine learning engineer with experience in Python and TensorFlow"

    # Act
    feedback = generate_feedback(sample_text)

    # Assert
    assert feedback is not None
    assert isinstance(feedback, dict)
    assert "strengths" in feedback
    assert "weaknesses" in feedback

