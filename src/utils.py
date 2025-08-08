import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pandas as pd
import numpy as np
import pickle

from src.components.exception import CustomException
from src.components.logger import setup_logger
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV


def evaluate_model(x_train, y_train, x_test, y_test, models: dict, param:  dict):
    try:
        report = {}
        best_model_obj = None
        best_score = 0
        best_model_name = None

        for model_name, model in models.items():
            param_grid = param.get(model_name, {})
            gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)
            gs.fit(x_train, y_train)
            best_model = gs.best_estimator_

            y_test_pred = best_model.predict(x_test)
            test_score = accuracy_score(y_test, y_test_pred)

            report[model_name] = test_score

            if test_score > best_score:
                best_score = test_score
                best_model_obj = best_model
                best_model_name = model_name

        return report, best_model_obj, best_model_name

    except Exception as e:
        raise Exception(f"Error in evaluate_models: {str(e)}")



#  save object
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
#  load object
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)