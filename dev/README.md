## Create Environment
```
cd XGBoost-MLOps-Pipeline\dev\
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## Run MLFlow UI
```
mlflow ui
```

## Select Best Model from MLFlow
```
mlflow artifacts download -r <run_id> -a model -d .\artifacts\
```
