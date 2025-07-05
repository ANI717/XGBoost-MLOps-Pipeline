## Create Environment
```
cd XGBoost-MLOps-Pipeline\model\
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## Run Pytest
Coverage should be over 85%
```
pytest --cov=src
```

## Package as Wheel File
```
pip install --upgrade build setuptools
python -m build
```