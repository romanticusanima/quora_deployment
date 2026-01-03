from pydantic import BaseModel

class PredictRequest(BaseModel):
    question1: str
    question2: str

    class Config:
        json_schema_extra = {
            "example": {
                "question1": "What is practical management and what is strategic management?",
                "question2": "What are the practical aspects of strategic management?"
            }
        }

class PredictResponse(BaseModel):
    class_name: str
    confidence: float

    class Config:
        json_schema_extra = {
            "example": {
                "class_name": "not_duplicate",
                "confidence": 0.856234
            }
        }
