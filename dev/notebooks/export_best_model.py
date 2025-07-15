#!/usr/bin/env python
# coding: utf-8

# ## Import Modules

# In[16]:


import os
import mlflow
import shutil
import pickle
import xgboost as xgb


# ## Import Model From MLFlow

# In[ ]:


run_id = "36d3b356719f4f7b920701953e523067"


# In[ ]:


mlruns_directory = os.path.join(os.getcwd(), "..", "mlruns")
mlflow.set_tracking_uri(f"file:{mlruns_directory}")


# In[15]:


model_uri = f"runs:/{run_id}/model"
mlflow.artifacts.download_artifacts(model_uri, dst_path="../artifacts")


# ## Export Model as Pickle

# In[19]:


# Load the XGBoost model from native format
model_path = os.path.join(os.getcwd(), "..", "artifacts", "model", "model.xgb")
model = xgb.Booster()
model.load_model(model_path)


# In[21]:


# Save as pickle
pickle_path = os.path.join(os.getcwd(), "..", "..", "model", "src", "xgboost_predictor", "artifacts", "model.pkl")
with open(pickle_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model converted and saved to: {pickle_path}")

