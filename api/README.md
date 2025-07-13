# 🚀 XGBoost Model Serving API

This module serves a trained **XGBoost** model via a **FastAPI** REST API, packaged as a Python wheel and deployable to Docker or Kubernetes.

---

## 📦 Features

- 🔁 Loads a trained XGBoost model from a Python wheel
- ⚡ Serves real-time predictions via FastAPI
- 🧩 Adds request ID middleware for traceability
- 🧠 Validates request/response schema with custom exception handlers
- 📄 Logs with file/console handlers including request ID, file, and line number

---

## ⚙️ Environment Setup

```bash
# Navigate to the API module directory
cd XGBoost-MLOps-Pipeline\api\

# Create and activate a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install required dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the API Server
```bash
hypercorn main:app
```
> `hypercorn` to support HTTP/2

---

## 📬 Example API Request
**POST** `/predict`</br>
**Request Body:**
```
{
  "features": [0.1, 1.2, 3.4, ..., 0.5]  // 30 floats
}
```
**Response:**
```json
{
  "prediction": 1
}
```

---

## 🐳 Docker Deployment
```bash
# Build Docker image
docker build -t xgboost-api .

# Run the container
docker run -d -p 8080:8080 --name xgboost-container xgboost-api
```
