import pymongo
import os
from src.Credential.CREDENTIAL import MONGO_DB_URL

import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        #MONGO_DB_URL = ""
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)   # pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
        self.db_name="ineuron"  #check name of db in mongodb where we wanna to store that data in mogodb database name

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
