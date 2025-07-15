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
docker build --no-cache -t xgboost-api-image:local .

# Run the container
docker run -d -p 8080:8080 --name xgboost-api-container xgboost-api-image
```

---

## 🚀 Kubernetes Deployment
This section outlines how to deploy the XGBoost Model Serving API to a local Kubernetes cluster using `Docker`, `Ingress-NGINX`, and `kubectl`.

### ✅ Prerequisites
- Docker Desktop with Kubernetes enabled
- kubectl installed and configured
- Docker daemon running
- Internet access to install Ingress controller

### 📥 1. Install Ingress NGINX Controller
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.1/deploy/static/provider/cloud/deploy.yaml
```
> Installs NGINX Ingress controller which is required for routing HTTP traffic to the API.

### 🛠 2. Build Docker Image
```bash
docker build --no-cache -t xgboost-api-image:local .
```
> Builds a local Docker image named `xgboost-api-image:local`. Needs to make sure this matches the `image:` in `deployment.yaml`.

### 📦 3. Deploy Resources Using Kustomize
```bash
kubectl apply -k ./k8s
```
> Applies all manifests (Deployment, Service, Ingress) under the `./k8s` folder using Kustomize.

### 🔍 4. Inspect Cluster Resources
```bash
kubectl get pods
kubectl get deployments
kubectl get svc
```
> Verifies that all components are running and available.

### 🪵 5. Debugging & Troubleshooting
```bash
# View Logs
kubectl logs <pod-name>

# Access Pod Shell
kubectl exec -it <pod-name> -- sh
```

### 🌐 6. Access the API
```arduino
http://localhost/xgboost-api/docs
```
> The Swagger UI of from FastAPI app should show up here

### 🧹 7. Clean Up Resources
```bash
kubectl delete -k ./k8s
```
> Safely removes deployment, service, and ingress related to this app.