import sys
import pytest
import logging
import numpy as np


sys.path.append("src")


@pytest.mark.initialization
def test_model_initialization():
    from xgboost_predictor.model import XGBoostPredictor
    
    # Test successful initialization
    model = XGBoostPredictor()
    assert model is not None

    # Test initialization with non-existent model path
    with pytest.raises(FileNotFoundError):
        XGBoostPredictor(model_path="non_existent_model.pkl")

    # Test initialization with invalid model file
    with pytest.raises(RuntimeError):
        XGBoostPredictor(model_path="pytest.ini")


@pytest.mark.prediction
def test_model_prediction():
    from xgboost_predictor.model import XGBoostPredictor
    
    model = XGBoostPredictor()
    
    # Test prediction with valid input
    sample = np.random.rand(30)  # Breast cancer dataset has 30 features
    prediction = model.predict(sample)
    assert isinstance(prediction, int)
    
    # Test prediction with invalid input (wrong size)
    with pytest.raises(ValueError):
        model.predict(np.random.rand(29))  # Should raise ValueError for wrong size
