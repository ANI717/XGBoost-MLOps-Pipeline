from pydantic import BaseModel, Field
from typing import List


class PredictionInput(BaseModel):
    features: List[float] = Field(..., min_items=30, max_items=30, description="List of 30 float features")
    
    class Config:
        extra = "forbid"
