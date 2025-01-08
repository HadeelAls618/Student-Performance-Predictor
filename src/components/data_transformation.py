#import libraies
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

#define class config
#The @dataclass decorator simplifies the creation of classes designed to store data
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    #we write the oprations we do here like trating missing values, one hot encoder and so on 
    def get_data_transformer_object(self):
        try:
            #we split the numurical and categorical features so we can perform opratioon on them
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipline=Pipeline(
                steps=[("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())]
            )
            cat_pipeline=Pipeline(
                steps=[('imputer',SimpleImputer(strategy="most_frequent")), ('one_hot_encoder',OneHotEncoder()),('scaler',StandardScaler(with_mean=False))]
            )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            #we created the piplines and now we need to compine them by using columntransform
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipline,numerical_columns),
                ('cat_pipeline', cat_pipeline,categorical_columns)
            ])
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
            
            #now we will create the function thaat will perform the entire workflow
            #the output of data ingestion
    def initiate_data_transformation(self,train_path,test_path):
        try:
                 
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
                 #creating the objoect
            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

                 #xtrain
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
                 #ytrain
            target_feature_train_df=train_df[target_column_name]

                 #xtest
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
                 #ytest
            target_feature_test_df=test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")
                 #apply the prosses
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            #concatinate the xtrain and the the ytrain
            train_arr = np.c_[
            input_feature_train_arr, np.array(target_feature_train_df)
            ]
            #concatinate the xtest and ytest
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            #save the prerosser using the save_object function defiend in utlies file, so we can accese it any time
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessing_obj)
            
            return (train_arr,
            test_arr,
            self.data_transformation_config.preprocessor_obj_file_path)


        except Exception as e:
             raise CustomException(e,sys)
             

