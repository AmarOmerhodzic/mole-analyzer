from pydantic import BaseModel

class MolePredictionResponse(BaseModel):
    result: str
    confidence: float
