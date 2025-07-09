from fastapi import APIRouter, HTTPException
from api.config import logger
from api.schemas.input_schema import PredictionInput
from api.schemas.output_schema import PredictionOutput
from xgboost_predictor.model import XGBoostPredictor
import numpy as np

router = APIRouter()
model = XGBoostPredictor()

@router.post("/predict", response_model=PredictionOutput, tags=["xgboost"])
async def predict_router(inputs: PredictionInput) -> PredictionOutput:
    """
    Predict endpoint for XGBoost model.
    Accepts: 30-feature float vector.
    Returns: Predicted class label (0 or 1).
    """
    try:
        features = np.array(inputs.features)
        prediction = model.predict(features)
    except Exception as e:
        logger.exception("Error occurred during prediction")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed due to an internal error: {str(e)}"
        )

    return PredictionOutput(prediction=prediction)
