#!/usr/bin/env python3
"""
Test Runner for AI Resume Analysis Model
This script runs comprehensive end-to-end tests for the AI model pipeline.
"""

import sys
import os
import subprocess
from pathlib import Path

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirement.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False
    return True

def run_tests():
    """Run the end-to-end tests"""
    print("🧪 Running end-to-end tests...")
    print("=" * 60)
    
    try:
        # Run tests with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_endtoend_model.py", 
            "-v", 
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
            return True
        else:
            print("❌ Some tests failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

def run_simple_test():
    """Run a simple integration test"""
    print("\n🔍 Running simple integration test...")
    
    try:
        # Import the main components
        from ai_models.skills_extractor import extract_and_normalize
        from ai_models.job_matcher import match_jobs
        from ai_models.career_recommender import recommend_career
        from ai_models.feedback_generator import generate_feedback
        
        # Test data
        test_resume = """
        Software Engineer with 5 years of experience in Python, JavaScript, 
        React, AWS, Docker, and Machine Learning. Experienced in building 
        scalable web applications and data pipelines.
        """
        
        print("📝 Test resume text:")
        print(test_resume.strip())
        print("\n" + "="*50)
        
        # Step 1: Extract skills
        print("1️⃣ Extracting skills...")
        skills = extract_and_normalize(test_resume)
        print(f"   Extracted skills: {skills}")
        
        # Step 2: Match jobs
        print("\n2️⃣ Matching jobs...")
        parsed_resume = {"raw_text": test_resume}
        matches = match_jobs(parsed_resume)
        print(f"   Top job matches: {matches[:2]}")
        
        # Step 3: Career recommendations
        print("\n3️⃣ Generating career recommendations...")
        recommendations = recommend_career(skills)
        print(f"   Career recommendations: {recommendations}")
        
        # Step 4: Generate feedback
        print("\n4️⃣ Generating feedback...")
        feedback = generate_feedback(skills, matches, recommendations)
        print(f"   Feedback: {feedback}")
        
        print("\n✅ Simple integration test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error in simple test: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function to run all tests"""
    print("🚀 AI Resume Analysis Model - End-to-End Testing")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists("main_ai.py"):
        print("❌ Please run this script from the project root directory")
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Run simple test first
    if not run_simple_test():
        print("❌ Simple test failed. Stopping.")
        return
    
    # Run comprehensive tests
    if not run_tests():
        print("❌ Comprehensive tests failed.")
        return
    
    print("\n🎉 All tests completed successfully!")
    print("\n📊 Test Summary:")
    print("   ✅ Dependencies installed")
    print("   ✅ Simple integration test passed")
    print("   ✅ Comprehensive end-to-end tests passed")
    print("\n🚀 Your AI model is ready to use!")

if __name__ == "__main__":
    main() 