# 🚀 XGBoost MLOps Pipeline

A complete end-to-end machine learning pipeline built using **XGBoost**, demonstrating model development, packaging, API serving, and deployment to Kubernetes.

---

## 📌 Key Components

- 🔬 **Model Training** with MLflow experiment tracking
- 📦 **Model Packaging** as a Python wheel for reusability
- ⚡ **Model Serving** via a FastAPI application
- 🐳 **Containerization** with Docker
- ☸️ **Deployment** to a local or cloud Kubernetes cluster

---

## 📁 Project Structure

- [`dev/`](./dev) – Model development and training with MLflow  
- [`model/`](./model) – Packaging trained model into a Python wheel  
- [`api/`](./api) – Serving predictions via FastAPI

---

## 🧠 Tech Stack

- `XGBoost` for model training  
- `MLflow` for experiment tracking  
- `FastAPI` for serving the model  
- `Docker` for containerization  
- `Kubernetes` for orchestration  
- `Pytest` for testing with coverage  
- `Logging`, `RequestID`, and `Validation` middleware for observability
