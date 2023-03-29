import os
import pandas as pd
from dataclasses import dataclass
from src.logger import lg
from src.exception import CustomException
from src.components import data_collection
import mysql.connector as conn
import sys

@dataclass
class DataStoringConfig:
    host: str="localhost"
    user: str=open('src/components/conf.py', 'r').readlines()[1].rstrip().split("=")[1]
    passwd: str=open('src/components/conf.py', 'r').readlines()[2].rstrip().split("=")[1]

class DataStoring:
    def __init__(self):
        self.storing_config = DataStoringConfig()

    def initiate_data_storing(self):
        lg.info("Entered Data storing Collection")
        try:
            # creating object of data collection class
            data_collection_obj = data_collection.DataCollection()

            # All data
            self.channel_statistics , self.all_stats = data_collection_obj.initiate_data_collection()
        except Exception as e:
            raise CustomException(e,sys)
    def sql_storing(self):
        lg.info("Begin to store data in SQL")
        try:
            mydb = conn.connect(
                host=self.storing_config.host,
                user=self.storing_config.user,
                passwd=self.storing_config.passwd
            )
            cursor = mydb.cursor()
            cursor.execute("show databases")
            # Fetching all the queries output
            print(cursor.fetchall())
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataStoring()
    obj.sql_storing()