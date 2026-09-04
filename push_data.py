import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

## to get env variable
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# certifi is a python package that provides a collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It is used to ensure secure connections when making HTTPS requests in Python applications.

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    ## this function will initialize the class and create the connection with mongodb
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    ## this function will convert the csv file to json format and return the records in list of dictionary format
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            # convert the dataframe to json format and return the records in list of dictionary format
            records=list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    ## this function will insert the records in mongodb collection and return the number of records inserted
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="Network_Security"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
