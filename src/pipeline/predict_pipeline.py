import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import setup_logger
from src.utils import load_object

class PredictPipeline:  
    def __init__(self):
        self.logger = setup_logger(__name__)
        self.logger.info("Predict Pipeline initiated")
    def predict(self, features):
        try:
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)
            self.logger.info("Preprocessor and model loaded successfully")
            
            # Transform features
            transformed_features = preprocessor.transform(features)
            
            # Make prediction
            prediction = model.predict(transformed_features)
            return prediction
            
        except Exception as e:
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self, 
                 Time_spent_Alone: float,
                    Stage_fear: float,
                    Social_event_attendance: float,
                    Going_outside: float,
                    Drained_after_socializing: float,
                    Friends_circle_size: float,):
        self.Time_spent_Alone = Time_spent_Alone
        self.Stage_fear = Stage_fear
        self.Social_event_attendance = Social_event_attendance
        self.Going_outside = Going_outside
        self.Drained_after_socializing = Drained_after_socializing
        self.Friends_circle_size = Friends_circle_size
        self.Post_frequency = Post_frequency
        
    def get_data_as_dataframe(self):
        try:
            data_dict = {
                "Time_spent_Alone": [self.Time_spent_Alone],
                "Stage_fear": [self.Stage_fear],
                "Social_event_attendance": [self.Social_event_attendance],
                "Going_outside": [self.Going_outside],
                "Drained_after_socializing": [self.Drained_after_socializing],
                "Friends_circle_size": [self.Friends_circle_size],
                "Post_frequency": [self.Post_frequency]
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            self.logger.error(f"Error in get_data_as_dataframe: {str(e)}")
            raise CustomException(e, sys)
                    
