## ⚙️ Environment Setup

```bash
# Navigate to the model packaging directory
cd XGBoost-MLOps-Pipeline\model\

# Create and activate a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install required dependencies
pip install -r requirements.txt
```


## 🧪 Run Tests with Coverage
Ensure unit test coverage is 85% or higher:
```bash
pytest --cov=src
```
> you can add `--cov-report=term-missing` to see which lines are not covered.


## 📦 Build Python Wheel
Upgrade build tools and package the project into a .whl and .tar.gz:
```bash
pip install --upgrade build setuptools
python -m build
```
> The distribution files will be created in the dist/ directory.
