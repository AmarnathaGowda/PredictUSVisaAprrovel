import os
from PredictUSVissaApproval.constants import DATABASE_NAME, MANGODB_URL_KEY
import pymongo
import certifi
from PredictUSVissaApproval.logger import logging
from PredictUSVissaApproval.exception import USvisaException
import sys

ca = certifi.where()

class MongoDBClinet:
    """
    Class Name  : export_data_inot_feature_store
    Description : This method exports the dataframe from mongbd feature store as dataframe

    Output      : connection to mongodb database
    On Failure  : raise an excpetion
    """

    clinet = None

    def __init__(self,database_name= DATABASE_NAME) -> None:
        try:
            if MongoDBClinet.clinet is None:
                mongo_db_url = os.getenv(MANGODB_URL_KEY)
                logging.info(f"MongoDBClinet URI : {mongo_db_url}")
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MANGODB_URL_KEY} is not set.")
                MongoDBClinet.clinet = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.clinet = MongoDBClinet.clinet
            self.database = self.clinet[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
            
        except Exception as e:
            raise USvisaException(e,sys)