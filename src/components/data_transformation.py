import sys
import os
import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.exception import CustomException
from src.logger import setup_logger
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_path: str = os.path.join('artifacts', 'preprocessor.pkl')
    preprocessed_train_data_path: str = os.path.join('artifacts', 'preprocessed_train.csv')
    preprocessed_test_data_path: str = os.path.join('artifacts', 'preprocessed_test.csv')
    
class DataTransformation: 
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("Data Transformation initiated")
    
    def initiate_data_transformation(self, train_data_path: str, test_data_path: str):
        try:
            # Load training and testing data
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            self.logger.info("Data loaded successfully for transformation")
            
            # Separate features and target variable
            x = train_df.drop('Personality', axis=1)
            y = train_df['Personality']
            X = test_df.drop('Personality', axis=1)
            Y = test_df['Personality']
            
            # Identify categorical and numerical columns
            cat_cols = x.select_dtypes(include=['object']).columns.tolist()
            num_cols = x.select_dtypes(include=['int64', 'float64']).columns.tolist()
           
            
            # Define preprocessing steps
            num_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ])
            
            cat_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])
            
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', num_transformer, num_cols),
                    ('cat', cat_transformer, cat_cols)
                ]
            )
            
            # Fit and transform
            x_transformed = preprocessor.fit_transform(x)
            X_transformed = preprocessor.transform(X)
            label_encoder = LabelEncoder()
            y_transformed = label_encoder.fit_transform(y)
            Y_transformed = label_encoder.transform(Y)

            # Save transformed arrays with target appended
            train_array = np.c_[x_transformed.toarray() if hasattr(x_transformed, "toarray") else x_transformed, y_transformed]
            test_array = np.c_[X_transformed.toarray() if hasattr(X_transformed, "toarray") else X_transformed, Y_transformed]
            
            # Get feature names after transformation
            feature_names = preprocessor.get_feature_names_out()

            # Append 'target' column
            column_names = list(feature_names) + ['Personality']
            train_df_transformed = pd.DataFrame(train_array, columns=column_names)

            
            # Save as CSVs
            train_df_transformed.to_csv(self.config.preprocessed_train_data_path, index=False)
            test_df_transformed = pd.DataFrame(test_array, columns=column_names)
            test_df_transformed.to_csv(self.config.preprocessed_test_data_path, index=False)
            
            self.logger.info("Transformed data saved successfully")
            
            # Save preprocessor
            save_object(file_path=self.config.preprocessor_path, obj=preprocessor)
            self.logger.info("Preprocessor saved successfully")
            
            save_object(file_path=os.path.join('artifacts', 'label_encoder.pkl'), obj=label_encoder)

            return (
                train_array,
                test_array
                
            )

        except Exception as e:
            raise CustomException(e, sys) from e



# if __name__ == "__main__":
#     config = DataTransformationConfig()
#     data_transformation = DataTransformation(config)
#     train_data_path = 'notebook/data/train.csv'
#     test_data_path = 'notebook/data/test.csv'
#     train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
#     print(f"✅ Preprocessor saved at: {config.preprocessor_path}")
#     print(f"✅ Transformed train data saved at: {config.preprocessed_train_data_path}")
#     print(f"✅ Transformed test data saved at: {config.preprocessed_test_data_path}")