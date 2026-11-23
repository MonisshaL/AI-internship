import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_FILE = "student_queries.csv"

def train_model():
    # Load the example dataset
    df = pd.read_csv(DATA_FILE)

    # Separate the text inputs and their correct category labels
    X = df["query"]
    y = df["category"]

    # Keep some examples aside to test the model
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # TF-IDF converts text into numerical features.
    # Logistic Regression learns to predict the category.
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n===== MODEL EVALUATION =====")
    print(f"Test accuracy: {accuracy:.2%}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions, labels=sorted(y.unique())))
    print("Category order:", sorted(y.unique()))

    return model

def main():
    model = train_model()

    print("\n===== STUDENT QUERY CLASSIFIER =====")
    print("Categories: Academic, Technical, Administrative, Placement")
    print("Type 'exit' to stop.")

    while True:
        query = input("\nEnter a student query: ").strip()

        if query.lower() == "exit":
            print("Thank you for trying the prototype!")
            break

        if not query:
            print("Please enter a question.")
            continue

        predicted_category = model.predict([query])[0]
        print("Predicted category:", predicted_category)

if __name__ == "__main__":
    main()
