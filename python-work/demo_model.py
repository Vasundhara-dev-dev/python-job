#!/usr/bin/env python3
"""
AI Resume Analysis Model - Demonstration Script
This script demonstrates how to use the AI model for resume analysis.
"""

import os
import sys
from main_ai import analyze_resume
from ai_models.skills_extractor import extract_and_normalize
from ai_models.job_matcher import match_jobs
from ai_models.career_recommender import recommend_career
from ai_models.feedback_generator import generate_feedback
from ai_models.resume_quality_predictor import predict_resume_quality

def demo_text_analysis():
    """Demonstrate analysis with text input"""
    print("🔍 TEXT ANALYSIS DEMO")
    print("=" * 50)
    
    # Sample resume text
    sample_resume = """
    JOHN DOE
    Software Engineer
    
    SKILLS:
    - Python, JavaScript, React, Node.js
    - AWS, Docker, Kubernetes, CI/CD
    - Machine Learning, TensorFlow, SQL
    - Git, Agile, REST APIs
    
    EXPERIENCE:
    - Senior Developer at TechCorp (2020-2023)
      * Built scalable microservices using Python and AWS
      * Led team of 5 developers in agile environment
      * Implemented CI/CD pipelines reducing deployment time by 60%
    
    - Data Scientist at AI Startup (2018-2020)
      * Developed ML models using TensorFlow and Python
      * Improved prediction accuracy by 25%
      * Created data pipelines processing 1M+ records daily
    
    EDUCATION:
    - BS Computer Science, University of Technology
    - MS Data Science, Online University
    """
    
    print("📝 Sample Resume:")
    print(sample_resume.strip())
    print("\n" + "="*50)
    
    # Step-by-step analysis
    print("\n1️⃣ SKILLS EXTRACTION")
    skills = extract_and_normalize(sample_resume)
    print(f"   Extracted skills: {skills}")
    
    print("\n2️⃣ JOB MATCHING")
    parsed_resume = {"raw_text": sample_resume}
    matches = match_jobs(parsed_resume)
    print("   Top job matches:")
    for i, match in enumerate(matches[:3], 1):
        print(f"   {i}. {match['job']} (Score: {match['score']:.3f})")
    
    print("\n3️⃣ CAREER RECOMMENDATIONS")
    recommendations = recommend_career(skills)
    print(f"   Recommended careers: {recommendations}")
    
    print("\n4️⃣ FEEDBACK GENERATION")
    feedback = generate_feedback(skills, matches, recommendations)
    print(f"   Feedback:\n{feedback}")
    
    print("\n5️⃣ QUALITY ASSESSMENT")
    quality = predict_resume_quality(sample_resume)
    print(f"   Resume quality: {quality}")
    
    return {
        "skills": skills,
        "matches": matches,
        "recommendations": recommendations,
        "feedback": feedback,
        "quality": quality
    }

def demo_file_analysis(file_path):
    """Demonstrate analysis with file input"""
    print(f"🔍 FILE ANALYSIS DEMO: {file_path}")
    print("=" * 50)
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None
    
    try:
        result = analyze_resume(file_path)
        
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            return None
        
        print("✅ Analysis completed successfully!")
        print("\n📊 RESULTS:")
        print(f"   Skills: {result['skills']}")
        print(f"   Top job match: {result['job_matches'][0]['job'] if result['job_matches'] else 'None'}")
        print(f"   Career recommendations: {result['career_recommendations']}")
        print(f"   Quality: {predict_resume_quality(result['parsed_text'])}")
        print(f"\n📝 Feedback:\n{result['feedback']}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return None

def demo_multiple_scenarios():
    """Demonstrate different resume scenarios"""
    print("🔍 MULTIPLE SCENARIOS DEMO")
    print("=" * 50)
    
    scenarios = [
        {
            "title": "Data Scientist Resume",
            "text": """
            Data Scientist with 3 years experience in Python, TensorFlow, 
            pandas, numpy, SQL, and machine learning. Built predictive models 
            for customer behavior analysis and recommendation systems.
            """
        },
        {
            "title": "Frontend Developer Resume", 
            "text": """
            Frontend Developer skilled in React, JavaScript, HTML, CSS, 
            TypeScript, and modern web development tools. Experience with 
            responsive design and user experience optimization.
            """
        },
        {
            "title": "DevOps Engineer Resume",
            "text": """
            DevOps Engineer with expertise in AWS, Docker, Kubernetes, 
            CI/CD pipelines, Terraform, and cloud infrastructure. 
            Experienced in automation and infrastructure as code.
            """
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario['title']}")
        print("-" * 30)
        
        skills = extract_and_normalize(scenario['text'])
        parsed = {"raw_text": scenario['text']}
        matches = match_jobs(parsed)
        recommendations = recommend_career(skills)
        feedback = generate_feedback(skills, matches, recommendations)
        quality = predict_resume_quality(scenario['text'])
        
        print(f"   Skills: {skills}")
        print(f"   Top match: {matches[0]['job'] if matches else 'None'}")
        print(f"   Recommendations: {recommendations}")
        print(f"   Quality: {quality}")
        print(f"   Feedback: {feedback[:100]}...")

def interactive_demo():
    """Interactive demo with user input"""
    print("🔍 INTERACTIVE DEMO")
    print("=" * 50)
    
    print("Enter your resume text (or type 'quit' to exit):")
    print("(You can paste a resume or just describe your skills)")
    
    while True:
        try:
            user_input = input("\n📝 Resume text: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                print("❌ Please enter some text.")
                continue
            
            print("\n🔄 Analyzing...")
            
            # Analyze the input
            skills = extract_and_normalize(user_input)
            parsed = {"raw_text": user_input}
            matches = match_jobs(parsed)
            recommendations = recommend_career(skills)
            feedback = generate_feedback(skills, matches, recommendations)
            quality = predict_resume_quality(user_input)
            
            # Display results
            print("\n📊 ANALYSIS RESULTS:")
            print(f"   Skills detected: {skills}")
            print(f"   Best job match: {matches[0]['job'] if matches else 'None'}")
            print(f"   Career recommendations: {recommendations}")
            print(f"   Resume quality: {quality}")
            print(f"\n💡 Feedback:\n{feedback}")
            
            # Ask if user wants to continue
            continue_choice = input("\nAnalyze another resume? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("👋 Thanks for using the AI Resume Analyzer!")
                break
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main demonstration function"""
    print("🚀 AI Resume Analysis Model - Demonstration")
    print("=" * 60)
    
    print("\nChoose a demo option:")
    print("1. Text Analysis Demo")
    print("2. File Analysis Demo (if you have a resume file)")
    print("3. Multiple Scenarios Demo")
    print("4. Interactive Demo")
    print("5. Run All Demos")
    
    try:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            demo_text_analysis()
        elif choice == "2":
            file_path = input("Enter the path to your resume file: ").strip()
            demo_file_analysis(file_path)
        elif choice == "3":
            demo_multiple_scenarios()
        elif choice == "4":
            interactive_demo()
        elif choice == "5":
            print("\n" + "="*60)
            demo_text_analysis()
            print("\n" + "="*60)
            demo_multiple_scenarios()
            print("\n" + "="*60)
            print("📁 For file analysis, you can run:")
            print("   python demo_model.py --file path/to/your/resume.pdf")
        else:
            print("❌ Invalid choice. Please run the script again.")
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Check for command line arguments
    if len(sys.argv) > 2 and sys.argv[1] == "--file":
        demo_file_analysis(sys.argv[2])
    else:
        main() 