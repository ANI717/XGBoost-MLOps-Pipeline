import os
import joblib
import logging
import numpy as np
import xgboost as xgb


model_path = f"{os.path.dirname(__file__)}/artifacts/model.pkl"


class XGBoostPredictor:
    def __init__(self, model_path: str = model_path, logger: logging.Logger = logging.getLogger(__name__)):
        """
        Initialize the XGBoost predictor with the path to the model file.

        :param model_path: Path to the trained XGBoost model file.
        :param logger: Logger instance for logging.
        """
        self.logger = logger

        if not os.path.exists(model_path):
            message = f"Model file not found at {model_path}"
            self.logger.error(message)
            raise FileNotFoundError(message)
        try:
            self.logger.info(f"Loading model from {model_path}")
            self.model = joblib.load(model_path)
        except Exception as e:
            message = f"Error loading model from {model_path}: {e}"
            self.logger.error(message)
            raise RuntimeError(message)


    def predict(self, features: np.ndarray) -> int:
        """
        Make predictions using the loaded XGBoost model.

        :param features: Input features for prediction. Size = (30,).
        :return: Predicted values.
        """

        if len(features) != 30:
            message = "Input features must have exactly 30 elements."
            self.logger.error(message)
            raise ValueError(message)

        try:
            dmatrix = xgb.DMatrix(features.reshape(1, -1))
            prediction = self.model.predict(dmatrix)
            return int(prediction[0])
        except Exception as e:
            message = f"Error making prediction: {e}"
            self.logger.error(message)
            raise RuntimeError(message)

