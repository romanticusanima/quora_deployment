import os
from typing import Tuple

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_DIR = os.getenv("MODEL_DIR", "zvonovska/quora-pairs-distilbert")
DEVICE = os.getenv("DEVICE", "cpu")

_tokenizer = None
_model = None

def load_model():
    global _tokenizer, _model
    if _tokenizer is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    if _model is None:
        _model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
        _model.to(DEVICE)
        _model.eval()

def predict(q1: str, q2: str) -> Tuple[str, float]:
    load_model()

    inputs = _tokenizer(
        q1,
        q2,
        truncation=True,
        max_length=128,
        return_tensors="pt"
    ).to(DEVICE)

    with torch.no_grad():
        out = _model(**inputs)
        probs = torch.softmax(out.logits, dim=-1).squeeze(0)

    # Works for binary or multi-class:
    pred_id = int(torch.argmax(probs).item())
    confidence = float(probs[pred_id].item())

    # Prefer labels from config if present; otherwise fallback:
    id2label = getattr(_model.config, "id2label", None) or {}
    class_name = id2label.get(pred_id, str(pred_id))

    return class_name, confidence
