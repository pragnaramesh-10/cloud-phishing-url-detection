import joblib
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

SCRIPT_DIR = Path(__file__).resolve().parent
MODEL_PATH = SCRIPT_DIR / "phishing_model.pkl"

model = joblib.load(MODEL_PATH)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class URLRequest(BaseModel):
    url: str


@app.get("/")
def root():
    return "API is running"


@app.post("/predict")
def predict(request: URLRequest):

    url = request.url.lower()

    suspicious_keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "bank",
        "paypal",
        "free",
        "bonus",
        "win"
    ]

    if any(word in url for word in suspicious_keywords):
        label = "phishing"
    else:
        label = "legitimate"

    return {
        "url": request.url,
        "prediction": label
    }