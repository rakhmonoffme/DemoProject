import os 
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.logger import setup_logger
from src.components.exception import CustomException
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('notebook', 'data', 'train.csv')    # Path to save training data
    test_data_path: str = os.path.join('notebook', 'data', 'test.csv')
    raw_data_path: str = os.path.join('notebook', 'data', 'raw.csv')
    
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config    # Initialize with the configuration
        # Set up logger for data ingestion
        self.logger = setup_logger(__name__)
    
    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv('notebook/data/personality_dataset.csv')
            self.logger.info("Data loaded successfully")
            
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True) # Ensure directory exists
            df.to_csv(self.config.raw_data_path, index=False)   # Save raw data
            self.logger.info("Raw data saved successfully") 
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False)  # Save training data
            test_set.to_csv(self.config.test_data_path, index=False)    # Save test data
            self.logger.info("Train and test data saved successfully")
            
            return self.config.train_data_path, self.config.test_data_path
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
if __name__ == "__main__":
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config)
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    print(f"Train data saved at: {train_data_path}")
    print(f"Test data saved at: {test_data_path}")