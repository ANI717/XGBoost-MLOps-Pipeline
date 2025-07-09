from pydantic import BaseModel


class PredictionOutput(BaseModel):
    prediction: int

    class Config:
        extra = "forbid"
