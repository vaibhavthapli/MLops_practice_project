from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestionConfig, DataIngestion
from src.mlproject.components.data_transformation import DataTransformation, DataTransformationConfig

if __name__ == "__main__":
    logging.info("Test")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        #data_ingestion.initiate_data_ingestion() #when run only ingestion.py
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion() # run for complete model

        data_transformation_config=DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path,test_data_path)


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)