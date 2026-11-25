# AI-Based Student Query Classification System

## 1. Project Overview

The AI-Based Student Query Classification System is a beginner-friendly AI application that helps categorize student questions automatically.

Students often have questions related to academics, technical issues, administration, and placements. Manually sorting these questions can take time.

This application uses Machine Learning and Natural Language Processing (NLP) to identify the category of a student's question.

The application also provides a confidence score to help users understand how certain the model is about its prediction.

## 2. Problem Statement

Educational institutions receive many student queries every day.

These queries may relate to:

- Academic information
- Technical support
- Administrative services
- Placement opportunities

Manually categorizing these queries can be time-consuming and may lead to delays in providing assistance.

The goal of this project is to develop an AI application that automatically classifies student queries into the appropriate categories.

## 3. Objectives

- Automate the classification of student queries.
- Reduce the effort required for manual categorization.
- Provide an easy-to-use interface for students and administrators.
- Display prediction confidence to help users understand the results.
- Handle invalid inputs and unexpected errors.

## 4. Methodology

The application follows these steps:

1. **Data collection:** A dataset containing sample student questions and their corresponding categories is used.
2. **Data preprocessing:** The text data is prepared for processing by the Machine Learning model.
3. **Model training:** The model learns patterns from the student questions and their categories.
4. **Prediction:** The trained model receives a new student question and predicts its category.
5. **Confidence-based output:** The application displays the predicted category and its confidence score.
6. **Error handling:** The application checks user inputs and handles invalid or unexpected inputs.

### Technologies Used

- Python – Programming language
- Pandas – Dataset handling
- Scikit-learn – Machine Learning
- Streamlit – User interface
- Natural Language Processing – Processing student questions

## 5. Main Features

- Automatic classification of student queries.
- Multiple query categories: Academic, Technical, Administrative, and Placement.
- Confidence-based prediction.
- Input validation and error handling.
- Simple and beginner-friendly interface.
- Ability to test the model using new student questions.

## 6. Demo

The application allows users to enter a student question and view the predicted category.

### Example

**Input:**

"When is the semester exam?"

**Expected category:**

Academic

**Input:**

"I cannot log in to the college portal."

**Expected category:**

Technical

### How to Run the Demo

1. Clone or download the GitHub repository.
2. Open the project folder in Command Prompt.
3. Install the required Python packages.
4. Run the Streamlit application.
5. Enter a student query and view the prediction.

The application can be demonstrated using the sample questions included in the dataset.

## 7. Installation and Execution

### Prerequisites

- Python 3.10 or a compatible Python version
- pip package manager
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd YOUR_PROJECT_FOLDER
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 8. Limitations

- The model's performance depends on the quality and size of the training dataset.
- It may misclassify questions that are very different from the training examples.
- The model may not understand complex questions or multiple questions in a single sentence.
- Confidence scores do not guarantee that a prediction is correct.
- The application does not provide official college information or resolve student queries directly.
- The model should be tested with a larger and more diverse dataset before real-world deployment.

## 9. Ethical Considerations

- Student queries should be handled responsibly and securely.
- Personal information such as student IDs, passwords, and private contact details should not be included in the training dataset.
- The application should not be used to make important decisions about students without human supervision.
- Predictions should be treated as suggestions rather than guaranteed answers.
- The system should be tested for incorrect predictions and potential bias.
- Users should be informed that their queries are processed by an AI system.

## 10. Future Improvements

- Expand the dataset with more student queries.
- Improve classification accuracy through further model evaluation.
- Support additional languages.
- Add a human review option for uncertain predictions.
- Integrate the system with a college helpdesk.
- Add a feature to suggest relevant answers to student queries.

## 11. Conclusion

The AI-Based Student Query Classification System demonstrates how Machine Learning can be used to automate the categorization of student questions.

The project provides practical experience in Python, Natural Language Processing, Machine Learning, and application development.

It serves as a beginner-friendly demonstration of how AI can support educational institutions by organizing student queries more efficiently.

## 12. Author and Internship

**Internship Organization:** SWYNEX Technologies

**Project:** AI-Based Student Query Classification System

**Task:** Task 4 – Complete Beginner-Friendly AI Application

**Author:** L. Monissha


