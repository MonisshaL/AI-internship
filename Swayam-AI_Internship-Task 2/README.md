# AI-Based Student Query Classification System

## Project overview
This beginner-friendly prototype classifies a student's text query into one of four categories:
- Academic
- Technical
- Administrative
- Placement

It uses a supervised machine learning pipeline with TF-IDF text features and Logistic Regression.

## Dataset
`student_queries.csv` contains 80 example queries (20 per category). These are sample/synthetic examples created for this prototype, not real student records.

## Requirements
- Python 3.9 or later
- pip

## Setup and run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the prototype:

```bash
python app.py
```

5. Enter a student query when prompted. Type `exit` to close the program.

## Example input and output

Input:
`When will the semester exams begin?`

Expected category:
`Academic`

Input:
`I cannot log in to the student portal.`

Expected category:
`Technical`

Input:
`How can I get a bonafide certificate?`

Expected category:
`Administrative`

Input:
`Are there any internship opportunities for IT students?`

Expected category:
`Placement`

The exact prediction and test accuracy may vary if the dataset or model settings are changed.

## Model integration
- TF-IDF converts text into numerical features.
- Logistic Regression learns patterns from the labelled examples.
- Scikit-learn Pipeline combines preprocessing and classification.

## Evaluation
The program reserves 20% of the dataset for testing and prints test accuracy, precision, recall, F1-score, and a confusion matrix.

The dataset is small and illustrative. Its evaluation score should not be treated as proof of production-level performance. A larger, more diverse, carefully labelled dataset would be needed for real-world use.

## Limitations
- The model only predicts the four categories in the training data.
- Spelling mistakes, slang, very short queries, and queries covering multiple topics may reduce performance.
- The training examples are synthetic and may not represent how all students write.

## Privacy and API keys
This local prototype does not call an external AI API and does not require an API key. Do not add private student information to the sample dataset.
