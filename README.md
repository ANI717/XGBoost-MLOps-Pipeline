# XGBoost MLOps Pipeline
An end-to-end machine learning pipeline using **XGBoost** trained on the `sklearn` Breast Cancer dataset. This project demonstrates a full production workflow:

- Model training and evaluation

- Packaging as a Python wheel

- Serving via a FastAPI API

- Containerization and deployment to a Kubernetes cluster

## 📁 Project Structure
- [🔬 Model Development & Training](https://github.com/ANI717/XGBoost-MLOps-Pipeline/tree/main/dev) </br>
Training and evaluating the XGBoost model using MLflow for experiment tracking.

- [📦 Model Packaging](https://github.com/ANI717/XGBoost-MLOps-Pipeline/tree/main/model) </br>
Packaging the trained model into a Python wheel for easy reuse and deployment.

- [🚀 API Deployment](https://github.com/ANI717/XGBoost-MLOps-Pipeline/tree/main/api) </br>
Serving predictions via a FastAPI app, containerized with Docker, and deployed to Kubernetes.

## ✅ Tech Stack
- XGBoost for model training

- MLflow for experiment tracking

- FastAPI for model serving

- Docker for containerization

- Kubernetes for orchestration and deployment

