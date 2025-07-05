from setuptools import setup, find_packages


# Read the requirements from the requirements.txt file
install_requires = [
    'pytest==8.4.1',
    'pytest-cov==6.2.1',
    'scikit-learn==1.7.0',
    'xgboost==3.0.2'
]


setup(
    name='xgboost_predictor',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'xgboost_predictor': ['artifacts/*.pkl']},
    install_requires=install_requires,
    author='Your Name',
    description='XGBoost prediction package',
)
