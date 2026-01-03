from fastapi import FastAPI
from src.schemas import PredictRequest, PredictResponse
from src.model import predict, load_model

app = FastAPI(
    title="Question Pairs Duplicate Classification API",
    description="API for classifying question pairs using distilBERT"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API! This is an API for classifying question pairs using ML."}

@app.post("/predict", response_model=PredictResponse)
def predict_duplicate(payload: PredictRequest):
    is_duplicate, confidence = predict(payload.question1, payload.question2)
    return PredictResponse(
        class_name=is_duplicate,
        confidence=round(confidence, 6)
    )
