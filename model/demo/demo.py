import numpy as np
import logging

from xgboost_predictor.model import XGBoostPredictor


model = XGBoostPredictor(logger=logging.getLogger(__name__))
sample = np.random.rand(30)  # Breast cancer dataset has 30 features
print("Prediction:", model.predict(sample))
