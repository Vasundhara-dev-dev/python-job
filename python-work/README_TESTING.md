# AI Resume Analysis Model - End-to-End Testing Guide

This guide explains how to test the AI resume analysis model comprehensively, covering all components and integration points.

## 🚀 Quick Start

### Option 1: Automated Test Runner (Recommended)
```bash
python run_tests.py
```

This will:
- Install all required dependencies
- Run a simple integration test
- Execute comprehensive end-to-end tests
- Provide detailed output and results

### Option 2: Manual Testing
```bash
# Install dependencies
pip install -r requirement.txt

# Run tests with pytest
python -m pytest tests/test_endtoend_model.py -v
```

## 📋 Test Components

The end-to-end testing covers these components:

### 1. **Skills Extraction** (`ai_models/skills_extractor.py`)
- Extracts technical skills from resume text
- Normalizes skill names
- Handles edge cases (empty text, None, non-string inputs)

### 2. **Job Matching** (`ai_models/job_matcher.py`)
- Uses TF-IDF and cosine similarity
- Matches resume against job database
- Returns ranked job matches with scores

### 3. **Career Recommendations** (`ai_models/career_recommender.py`)
- Recommends career paths based on skills
- Uses skill matching algorithm
- Provides fallback recommendations

### 4. **Feedback Generation** (`ai_models/feedback_generator.py`)
- Generates personalized feedback
- Combines skills, job matches, and recommendations
- Provides actionable insights

### 5. **Resume Quality Prediction** (`ai_models/resume_quality_predictor.py`)
- Predicts resume quality (currently mocked)
- Can be extended with ML models

### 6. **File Parsing** (`ai_models/resume_parser.py`)
- Parses PDF and DOCX files
- Extracts text content
- Handles file format errors

## 🧪 Test Scenarios

### Individual Component Tests
```python
# Test skills extraction
from ai_models.skills_extractor import extract_and_normalize
skills = extract_and_normalize("Python developer with AWS experience")
print(skills)  # ['python', 'aws']

# Test job matching
from ai_models.job_matcher import match_jobs
matches = match_jobs({"raw_text": "Python developer..."})
print(matches)  # [{'job': 'Backend Developer', 'score': 0.85}, ...]

# Test career recommendations
from ai_models.career_recommender import recommend_career
recs = recommend_career(['python', 'aws'])
print(recs)  # ['Backend Developer', 'Data Scientist']

# Test feedback generation
from ai_models.feedback_generator import generate_feedback
feedback = generate_feedback(skills, matches, recs)
print(feedback)  # Detailed feedback string
```

### Complete Pipeline Test
```python
from main_ai import analyze_resume

# Test with a resume file
result = analyze_resume("path/to/resume.pdf")
print(result)
# Output: {
#   "parsed_text": "...",
#   "skills": ["python", "aws", ...],
#   "job_matches": [...],
#   "career_recommendations": [...],
#   "feedback": "..."
# }
```

## 📊 Test Coverage

The comprehensive test suite covers:

### ✅ **Functional Testing**
- Skills extraction accuracy
- Job matching relevance
- Career recommendation logic
- Feedback generation quality

### ✅ **Error Handling**
- Invalid file formats
- Empty or malformed inputs
- Missing dependencies
- File not found scenarios

### ✅ **Integration Testing**
- Complete pipeline flow
- Data flow between components
- Output format consistency
- Performance under load

### ✅ **Edge Cases**
- Empty resume text
- No skills detected
- No job matches found
- Invalid file paths

## 🔧 Test Configuration

### Environment Setup
```bash
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirement.txt

# Install test dependencies
pip install pytest pytest-cov
```

### Running Specific Tests
```bash
# Run only skills extraction tests
python -m pytest tests/test_endtoend_model.py::TestEndToEndModel::test_skills_extraction_pipeline -v

# Run with coverage
python -m pytest tests/test_endtoend_model.py --cov=ai_models --cov-report=html

# Run with detailed output
python -m pytest tests/test_endtoend_model.py -v -s
```

## 📈 Performance Testing

### Load Testing
```python
import time
from ai_models.skills_extractor import extract_and_normalize

# Test performance with large text
large_text = "Python " * 1000 + "AWS " * 500 + "Docker " * 300

start_time = time.time()
skills = extract_and_normalize(large_text)
end_time = time.time()

print(f"Processing time: {end_time - start_time:.2f} seconds")
print(f"Skills found: {len(skills)}")
```

### Memory Testing
```python
import psutil
import os

# Monitor memory usage during processing
process = psutil.Process(os.getpid())
initial_memory = process.memory_info().rss / 1024 / 1024  # MB

# Run your test here
skills = extract_and_normalize(large_text)

final_memory = process.memory_info().rss / 1024 / 1024  # MB
print(f"Memory usage: {final_memory - initial_memory:.2f} MB")
```

## 🐛 Debugging Tests

### Common Issues and Solutions

1. **Import Errors**
   ```bash
   # Make sure you're in the project root
   cd /path/to/python-work
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   ```

2. **Missing Dependencies**
   ```bash
   # Install all dependencies
   pip install -r requirement.txt
   ```

3. **File Path Issues**
   ```python
   # Use absolute paths for testing
   import os
   test_file = os.path.join(os.getcwd(), "tests", "sample_resume.pdf")
   ```

4. **Mock Dependencies**
   ```python
   # Mock external dependencies
   from unittest.mock import patch
   
   @patch('ai_models.resume_quality_predictor.predict_resume_quality')
   def test_with_mock(self, mock_predict):
       mock_predict.return_value = "Good"
       # Your test here
   ```

## 📝 Adding New Tests

### Test Structure
```python
def test_new_feature(self):
    """Test description"""
    # Arrange
    input_data = "test input"
    
    # Act
    result = your_function(input_data)
    
    # Assert
    assert isinstance(result, expected_type)
    assert len(result) > 0
    # Add more specific assertions
```

### Test Data
```python
@pytest.fixture
def sample_data(self):
    """Provide test data"""
    return {
        "resume_text": "Python developer...",
        "expected_skills": ["python", "aws"],
        "expected_jobs": ["Backend Developer"]
    }
```

## 🎯 Best Practices

1. **Test Isolation**: Each test should be independent
2. **Clear Assertions**: Use specific, meaningful assertions
3. **Error Testing**: Always test error conditions
4. **Performance**: Monitor test execution time
5. **Documentation**: Document complex test scenarios

## 📞 Support

If you encounter issues with testing:

1. Check the error messages carefully
2. Verify all dependencies are installed
3. Ensure you're in the correct directory
4. Run individual component tests first
5. Check the test logs for detailed information

## 🚀 Next Steps

After successful testing:

1. **Deploy the model** to production
2. **Monitor performance** in real-world usage
3. **Collect feedback** from users
4. **Iterate and improve** based on results
5. **Add more test cases** as features evolve 