import re
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.append("src")
from main import app  # your FastAPI app entrypoint


@pytest.mark.integration
def test_predict_integration_success():
    client = TestClient(app)

    payload = {
        "features": [0.1] * 30  # match your model's expected input
    }

    response = client.post("/predict", json=payload)

    # Check status
    assert response.status_code == 200

    # Validate response
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1]

    # Validate headers set by middlewares
    assert "request-id" in response.headers
    assert "process-time" in response.headers
    assert re.fullmatch(r"\d+\.\d{4,}", response.headers["process-time"])


@pytest.mark.integration
def test_predict_integration_bad_input():
    client = TestClient(app)

    payload = {"bad_key": [1, 2, 3]}

    response = client.post("/predict", json=payload)

    assert response.status_code == 400
