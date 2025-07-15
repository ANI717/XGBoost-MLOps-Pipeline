#!/usr/bin/env python
# coding: utf-8

# ## Import Modules

# In[2]:


import os
import mlflow
import mlflow.xgboost
import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ## Prepare Data

# In[3]:


# 1. Load data
data = load_breast_cancer()


# In[4]:


# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.2,
    random_state=717
    )


# ## Train XGBoost Model with MLFlow

# In[5]:


mlruns_directory = os.path.join(os.getcwd(), "..", "mlruns")
os.makedirs(mlruns_directory, exist_ok=True)


# In[6]:


# Set tracking URI to parent directory
mlflow.set_tracking_uri(f"file:{mlruns_directory}")


# In[7]:


# Create or set experiment
mlflow.set_experiment("xgboost-breast-cancer")


# In[9]:


with mlflow.start_run():

    # Define model and hyperparameters
    params = {
        "n_estimators": 150,
        "learning_rate": 0.1,
        "max_depth": 6,
        "eval_metric": "logloss",
        "random_state": 717
    }


    # Log hyperparameters
    mlflow.log_params(params)


    # Initialize the model
    model = xgb.XGBClassifier(**params)


    # Train the model
    model.fit(X_train, y_train)


    # Make predictions
    y_pred = model.predict(X_test)


    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)


    # Log metrics
    mlflow.log_metric("accuracy", accuracy)


    # Log model
    mlflow.xgboost.log_model(model, "model")


    print(f"Run complete. Accuracy: {accuracy:.4f}")

