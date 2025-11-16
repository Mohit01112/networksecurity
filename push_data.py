import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

# Your actual MongoDB connection string
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
print("MONGO_DB_URI:", MONGO_DB_URI)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            # Correct JSON format for MongoDB
            records = json.loads(data.to_json(orient="records"))
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Use TLS certificate for Atlas
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI, tlsCAFile=ca)

            db = self.mongo_client[self.database]
            col = db[self.collection]

            col.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = r"Network_Data\phishingData.csv"    # corrected file name
    DATABASE = "MOHITHAI"                          # your actual DB name
    COLLECTION = "NetworkData"                     # collection name

    networkobj = NetworkDataExtract()

    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)

    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(no_of_records)
