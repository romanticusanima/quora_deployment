# Quora Duplicate Question Detection API

A FastAPI-based web service that detects duplicate question pairs using a fine-tuned DistilBERT model.

## Model

This API uses a DistilBERT model fine-tuned on the Quora Question Pairs dataset to classify whether two questions are duplicates or not.

- **Model:** [zvonovska/quora-pairs-distilbert](https://huggingface.co/zvonovska/quora-pairs-distilbert)
- **Architecture:** DistilBERT for sequence classification
- **Task:** Binary classification (duplicate / not duplicate)

### API Usage

The deployed API can be accessed at: [link](https://quora-deployment.onrender.com/)
Use this endpoint to send requests and receive model predictions.

## API Endpoints

### `GET /`
Health check endpoint that returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the ML Model API! This is an API for classifying question pairs using ML."
}
```

### `POST /predict`
Predict whether two questions are duplicates.

**Request Body:**
```json
{
  "question1": "Why is beef banned in India and not pork as well?",
  "question2": "Is beef banned in India?"
}
```

**Response:**
```json
{
  "class_name": "not_duplicate",
  "confidence": 0.856234
}
```

### `GET /docs`
Interactive API documentation (Swagger UI)

## Running Locally

### Option 1: Using Docker

```bash
# Build the image
docker build -t quora-model .

# Run the container
docker run -p 8000:8000 -e PORT=8000 quora-model
```

### Option 2: Using Python directly

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000
```

**Note:** On first run, the model will be downloaded from Hugging Face (~255MB). This may take 2-3 minutes.

## Testing the API

### Using curl:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "question1": "How do I learn Python?",
    "question2": "What is the best way to learn Python?"
  }'
```

### Using the interactive docs:
Visit http://localhost:8000/docs and use the "Try it out" feature.


## Project Structure

```
.
├── app.py                 # FastAPI application
├── src/
│   ├── model.py          # Model loading and inference
│   └── schemas.py        # Pydantic models for API
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **Transformers** - Hugging Face transformers library
- **PyTorch** - Deep learning framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
