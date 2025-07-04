## Create Environment
```
cd xgboost-mlops-pipeline\model\
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## Run MLFlow UI
```
cd xgboost-mlops-pipeline\model\
mlflow ui
```

## Select Best Model from MLFlow
```
mlflow artifacts download -r <run_id> -a model -d ./models/xgboost_predictor/artifacts/
```
