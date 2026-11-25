# SWYNEX – AI-Based Student Query Classification System

A small ML prototype that classifies student questions into Academic, Technical, Administrative, or Placement categories.

## Intelligent feature
The app displays the highest predicted class probability and flags low-confidence predictions for human review. It validates empty, overly long, and non-word inputs and provides error messages.

**Important:** A confidence threshold is not a dependable out-of-scope detector. An unrelated query may still receive a confident category. The displayed confidence is not guaranteed to be calibrated.

## Run
Requires Python 3.9+.

```bash
pip install -r requirements.txt
streamlit run app.py
```

The browser interface accepts a query and displays a prediction. Expand **Model evaluation** to view accuracy, precision, recall, F1-score, and a confusion matrix.

## Examples and failure cases
See `evaluation_examples.csv`. It includes ordinary category examples, empty input, symbols-only input, an unrelated query, and a potentially ambiguous query.

## Evaluation
The model uses a stratified 75/25 train-test split with a fixed random seed. Metrics are calculated on the held-out split. The dataset contains a small number of synthetic examples; scores are illustrative and do not establish production performance.

## Limitations
- Only four trained categories are supported.
- Ambiguous, misspelled, slang, or unfamiliar queries may be misclassified.
- The model may assign an unrelated query to one of the four categories.
- More varied, human-labelled data and a separate evaluation set are needed for real deployment.

## Privacy
This local prototype does not use an external AI API. Do not enter private student information.
