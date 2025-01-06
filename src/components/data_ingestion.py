#import libraries
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass




#class data ingestion config
#Configuration parameters, like file paths, are stored in one place (DataIngestionConfig).
#pathss or inputs such as the path tp our raw data, train and test data

#you can use the '@dataclass' only when you want to define variebles in the class but if you want to define functions you can't use it
@dataclass
class DataIngestionConfig:
   train_data_path:str=os.path.join('artifacts','train.csv')
   test_data_path: str=os.path.join('artifacts',"test.csv")
   raw_data_path: str=os.path.join('artifacts',"data.csv")



#class data ingestion
#All methods related to loading, validating, and saving data are part of the DataIngestion class.
#read the data 

class DataIngestion:
   def __init__(self):
      self.ingestion_config=DataIngestionConfig()
   #the function that will defin the entire workflow of data ingestion
   #Note each opration we start here we store it in the log to keep track everything we do
   def initiate_data_ingestion(self):
      logging.info('enterned data ingestion')
      try:
         #reading thge data from the source the sourse can be API, database or anywhere
         df=pd.read_csv('src/Notebooks/data/stud.csv')
         logging.info('read the dataset as a dataframe')

         #extract the directory name and make sure it exist, if it is not create it
         os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

         #after reading the data from the source save the data as a raw data
         df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

         #now we take the data and split it into trant and test
         logging.info('train, test split initiated')
         train_set,test_set=train_test_split(df,test_size=0.2, random_state=42)
         #save the trandf and test data
         train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=False)
         test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=False)

         logging.info('data ingestion is completed')

         return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path )
      
      except Exception as e:
         raise CustomException(e,sys)



#to run the code 
if __name__=='__main__':
   obj=DataIngestion()
   obj.initiate_data_ingestion()

