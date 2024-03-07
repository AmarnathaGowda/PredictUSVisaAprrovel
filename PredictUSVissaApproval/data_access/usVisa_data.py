from PredictUSVissaApproval.configuration.mongo_db_connection import MongoDBClinet
from PredictUSVissaApproval.constants import DATABASE_NAME
from PredictUSVissaApproval.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np
from PredictUSVissaApproval.logger import logging

class USvisaData:
    """
    This class help to export entire mongo db records as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClinet(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e,sys)
        
    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collection as dataframe:
            return pd.DataFrame of collection
            """
            logging.info(f" USVisa_data.py Database name : {database_name}")
            
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            logging.info(f" USVisa_data.py Collaction name : {collection}")

            df = pd.DataFrame(list(collection.find()))
            logging.info(f"Dataframe legth : {df.shape}")
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e,sys)