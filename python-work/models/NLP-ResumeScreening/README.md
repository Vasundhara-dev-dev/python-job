# NLP-ResumeScreening
ResumeScreening


BUSINESS NEEDS: To screen the resume automatically that can predict the specific role according to the given resume description.

Data set was taken from Kaggle. It contains 976 records and 2 features (Category and Resume decription)

Developed a model using Multinomial Naïve Bayes Classifier to classify various resumes into 25 different job categories. The model has been trained and tested on the Kaggle dataset named ‘resume-dataset’ containing 961 resume entries. Data preprocessing, Stopwords removal, Stemming and Lemmatization is performed on this data along with vectorization using Count Vectorizer. The model gives us an accuracy of 98.7%.

Along with this, I created a deployable streamlit application for the same model to classify various Skillsets into the preferrable and appropriate job category.

https://jeevikaaanand-nlp-resumescreening-resume-app-09fxy7.streamlit.app/
