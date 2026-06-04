import joblib
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_PATH = SCRIPT_DIR / "dataset.csv"
MODEL_PATH = SCRIPT_DIR / "phishing_model.pkl"

df = pd.read_csv(DATASET_PATH)
df = df[df["type"].isin(["phishing", "benign"])].copy()
df["label"] = df["type"].map({"phishing": 1, "benign": 0})

X = df["url"]
y = df["label"]

model = Pipeline(
    [
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000)),
    ]
)

model.fit(X, y)
joblib.dump(model, MODEL_PATH)

print("Model trained successfully")
