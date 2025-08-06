from ai_models.resume_quality_predictor import predict_quality

def test_resume_quality_prediction():
    # Arrange
    sample_text = "Experienced Python Developer skilled in Flask and AWS"

    # Act
    result = predict_quality(sample_text)

    # Assert
    assert result is not None
    assert isinstance(result, dict)
    assert "quality" in result
    

