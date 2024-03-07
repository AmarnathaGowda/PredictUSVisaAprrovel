import sys
from PredictUSVissaApproval.exception import USvisaException
from PredictUSVissaApproval.logger import logging
from PredictUSVissaApproval.components.data_ingestion import DataIngestion
from PredictUSVissaApproval.entity.config_entity import (DataIngestionConfig)
from PredictUSVissaApproval.entity.artifact_entity import (DataIngestionArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """ 
        This method of TrainPipeline class is responsible for starting data ingenstion component
        """

        try:
            logging.info("Enteed the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongo database")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the strat_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise UserWarning(e, sys) from e

    def run_pipeline(self,) -> None:
        """
        This method of TrainPipeline class is reponsible for running complete pipline
        """

        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise USvisaException(e, sys)
        
        