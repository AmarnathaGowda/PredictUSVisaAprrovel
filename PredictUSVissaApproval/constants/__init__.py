import os 
from datetime import date

from dotenv import load_dotenv
import os
load_dotenv()

# MongoDBClient = os.getenv("MongoDBClient")

DATABASE_NAME = "US_VISAD"
COLLECTION_NAME = "visa_dataset"
MANGODB_URL_KEY = "MONGODB_URL"
PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str ="artifact"
MODEL_FILE_NAME ="model.pkl"
TARGET_COLUMN ="case_status"
CURRENT_YESR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME ="preprocessing.pkl"
FILE_NAME: str ="usvisa.csv"
TRAIN_FILE_NAME: str ="train.csv"
TEST_FILE_NAME: str ="test.csv"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_dataset"
DATA_INGESTION_DIR_NAME: str ="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str ="feature_store"
DATA_INGESTION_INGESTED_DIR: str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2