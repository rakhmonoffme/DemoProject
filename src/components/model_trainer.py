import os
import sys
from dataclasses import dataclass
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.utils import evaluate_model, save_object
from src.exception import CustomException
from src.logger import setup_logger


@dataclass
class ModelTrainerConfig:
    trained_model_path: str = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("Model trainer initiated")

    def initiate_model_trainer(self, train_array, test_array):
        try:
            self.logger.info("Splitting training and testing arrays")
            x_train, y_train = train_array[:, :-1], train_array[:, -1]
            x_test, y_test = test_array[:, :-1], test_array [:, -1]

            models = {
                "Random Forest": RandomForestClassifier(),
                "Logistic Regression": LogisticRegression(),
                "Support Vector Machine": SVC(),
                "Decision Tree": DecisionTreeClassifier(),
                "K-Nearest Neighbors": KNeighborsClassifier(),
                "XGBoost": XGBClassifier( eval_metric='logloss')
            }
            
            params = {
                "Random Forest": {
                    "n_estimators": [50, 100, 200],
                    "max_depth": [None, 10, 20],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4]
                },

                "Logistic Regression": {
                    "C": [0.01, 0.1, 1, 10, 100],
                    "solver": ["liblinear", "lbfgs"],
                    "penalty": ["l2"],
                    "max_iter": [100, 200]
                },

                "Support Vector Machine": {
                    "C": [0.1, 1, 10],
                    "kernel": ["linear", "rbf", "poly"],
                    "gamma": ["scale", "auto"]
                },

                "Decision Tree": {
                    "criterion": ["gini", "entropy", "log_loss"],
                    "max_depth": [None, 10, 20, 30],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4]
                },

                "K-Nearest Neighbors": {
                    "n_neighbors": [3, 5, 7, 9],
                    "weights": ["uniform", "distance"],
                    "metric": ["euclidean", "manhattan"]
                },

                "XGBoost": {
                    "learning_rate": [0.01, 0.05, 0.1],
                    "n_estimators": [50, 100, 200],
                    "max_depth": [3, 5, 7],
                    "subsample": [0.7, 0.8, 1.0]
                }
            }

            
            model_report, best_model, best_model_name = evaluate_model(
                x_train=x_train,
                y_train=y_train,
                x_test=x_test,
                y_test=y_test,
                models=models,
                param=params
            )

            best_model_accuracy = model_report[best_model_name]
            self.logger.info(f"✅ Best model: {best_model_name} with accuracy: {best_model_accuracy:.4f}")

            if best_model_accuracy > 0.6:
                self.logger.info("Model accuracy is above threshold. Saving the model...")
                save_object(file_path=self.config.trained_model_path, obj=best_model)
                self.logger.info(f"Model saved at: {self.config.trained_model_path}")
            else:
                self.logger.info("Model accuracy below threshold. Model not saved.")
            return accuracy_score(y_test, best_model.predict(x_test)), best_model_name

        except Exception as e:
            raise CustomException(e, sys)
