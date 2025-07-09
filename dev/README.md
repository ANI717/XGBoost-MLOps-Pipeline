## ⚙️ Environment Setup
```bash
# Navigate to the project directory
cd XGBoost-MLOps-Pipeline/dev/

# Create a virtual environment
python -m venv venv

# Activate the environment (Windows)
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

```

---

## 📊 Launch MLflow UI
```bash
mlflow ui

```
> This will start the MLflow tracking server at http://localhost:5000, where you can view experiment runs, parameters, metrics, and model artifacts.
