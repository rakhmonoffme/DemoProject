import os 
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.components.logger import setup_logger
from src.components.exception import CustomException
from src.components.data_transformation import DataTransformationConfig, DataTransformation
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('notebook', 'data', 'train.csv')
    test_data_path: str = os.path.join('notebook', 'data', 'test.csv')
    raw_data_path: str = os.path.join('notebook', 'data', 'raw.csv')

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.logger = setup_logger(__name__)
    
    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv('notebook/data/personality_dataset.csv')
            self.logger.info("Data loaded successfully")
            
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False)
            self.logger.info("Raw data saved successfully") 
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)
            self.logger.info("Train and test data saved successfully")
            
            return self.config.train_data_path, self.config.test_data_path
        
        except Exception as e:
            raise CustomException(e, sys) from e

if __name__ == "__main__":
    # Data Ingestion
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config)
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    print(f"Train data saved at: {train_data_path}")
    print(f"Test data saved at: {test_data_path}")
    
    # Data Transformation
    config = DataTransformationConfig()
    data_transformation = DataTransformation(config)
    train_array, test_array = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    print(f"✅ Preprocessor saved at: {config.preprocessor_path}")
    print(f"✅ Transformed train data saved at: {config.preprocessed_train_data_path}")
    print(f"✅ Transformed test data saved at: {config.preprocessed_test_data_path}")
    
    
    # Model Training
    model_trainer_config = ModelTrainerConfig()  # ✅ Instantiate
    model_trainer = ModelTrainer(model_trainer_config)
    model_trainer.initiate_model_trainer(train_array, test_array)
