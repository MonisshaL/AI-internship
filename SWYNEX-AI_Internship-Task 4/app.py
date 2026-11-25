import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

THRESHOLD = 0.45
MAX_CHARS = 500

@st.cache_resource
def train():
    df = pd.read_csv("student_queries.csv").dropna(subset=["query", "category"])
    df["query"] = df["query"].astype(str).str.strip()
    df = df[df["query"] != ""]
    if df["category"].nunique() < 2:
        raise ValueError("Dataset needs at least two categories.")
    x_train, x_test, y_train, y_test = train_test_split(
        df["query"], df["category"], test_size=0.25, random_state=42, stratify=df["category"])
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2), lowercase=True)),
        ("classifier", LogisticRegression(max_iter=1000))
    ])
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    return model, y_test, pred

def classify(model, text):
    if not isinstance(text, str) or not text.strip():
        return {"status":"error","message":"Enter a query before classifying."}
    text = text.strip()
    if len(text) > MAX_CHARS:
        return {"status":"error","message":f"Query must be {MAX_CHARS} characters or fewer."}
    if not any(ch.isalpha() for ch in text):
        return {"status":"error","message":"Enter words, not only numbers or symbols."}
    probs = model.predict_proba([text])[0]
    i = probs.argmax()
    result = {"category":str(model.classes_[i]),"confidence":float(probs[i])}
    result["status"] = "uncertain" if result["confidence"] < THRESHOLD else "success"
    return result

st.set_page_config(page_title="SWYNEX Student Query Classifier", page_icon="🎓")
st.title("🎓 Student Query Classifier")
st.write("Classify queries as Academic, Technical, Administrative, or Placement.")
try:
    model, y_test, pred = train()
except Exception as e:
    st.error(f"Could not train model: {e}")
    st.stop()

query = st.text_area("Enter a student query", max_chars=MAX_CHARS,
                     placeholder="When will the semester exams begin?")
if st.button("Classify query", type="primary"):
    result = classify(model, query)
    if result["status"] == "error":
        st.error(result["message"])
    elif result["status"] == "uncertain":
        st.warning("Low confidence. Please rephrase the query or ask a staff member.")
        st.write(f"Closest category: **{result['category']}**")
        st.write(f"Confidence: **{result['confidence']:.1%}**")
    else:
        st.success(f"Predicted category: {result['category']}")
        st.write(f"Confidence: **{result['confidence']:.1%}**")

with st.expander("Model evaluation"):
    st.metric("Held-out test accuracy", f"{accuracy_score(y_test,pred):.1%}")
    st.caption(f"Evaluation uses {len(y_test)} held-out examples. This small synthetic dataset is only a demo.")
    st.dataframe(pd.DataFrame(classification_report(y_test,pred,output_dict=True,zero_division=0)).transpose())
    labels=list(model.classes_)
    st.write("Confusion matrix (rows = actual, columns = predicted)")
    st.dataframe(pd.DataFrame(confusion_matrix(y_test,pred,labels=labels),index=labels,columns=labels))

st.caption("Confidence is not a guarantee of correctness. Do not enter private student information.")
