from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestionConfig, DataIngestion
from src.mlproject.components.data_transformation import DataTransformation, DataTransformationConfig
from src.mlproject.components.model_trainer import ModelTrainer, ModelTrainerConfig



def run_training_pipeline():
    logging.info("Training pipeline")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        #data_ingestion.initiate_data_ingestion() #when run only ingestion.py
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion() # run for complete model

        #data_transformation_config=DataTransformationConfig()
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        ##model training

        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)


