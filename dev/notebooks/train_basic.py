#!/usr/bin/env python
# coding: utf-8

# ## Import Modules

# In[2]:


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


# ## Train XGBoost Model

# In[7]:


model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    eval_metric='logloss',
    random_state=717
    )


# In[8]:


model.fit(X_train, y_train)


# ## Predict and Evaluate

# In[9]:


y_pred = model.predict(X_test)


# In[12]:


accuracy = accuracy_score(y_test, y_pred)


# In[13]:


print(accuracy)

