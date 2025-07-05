import setuptools


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


with open("requirements.txt", 'r') as file:
    install_requires = [line.strip() for line in file if line.strip() and not line.startswith('#')]


setuptools.setup(
    name="xgboost_predictor",
    version="1.0.0",
    author="Animesh Bala Ani",
    author_email="animesh.ani@live.com",
    description="A package for XGBoost model prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ANI717/XGBoost-MLOps-Pipeline",
    project_urls={
        "Bug Tracker": "https://github.com/ANI717/XGBoost-MLOps-Pipeline/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=install_requires,
    package_data={'xgboost_predictor': ['artifacts/*.pkl']},
    include_package_data=True,
    python_requires=">=3.12",
)
