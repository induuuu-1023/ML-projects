import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging


class DataIngestion:
    def __init__(self, file_path=None):
        self.file_path = file_path or r"d:/mlproject/notebook/data/StudentsPerformance.csv"

    def initiate_data_ingestion(self, test_size=0.2, random_state=42):
        try:
            logging.info("Starting data ingestion...")

            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"CSV file not found at: {self.file_path}")

            df = pd.read_csv(self.file_path)
            logging.info(f"CSV loaded. Shape: {df.shape}")

            data = df.values

            train_array, test_array = train_test_split(
                data, test_size=test_size, random_state=random_state
            )

            return train_array, test_array

        except Exception as e:
            raise CustomException(e, sys)


# Debug check
if __name__ == "__main__":
    print("DataIngestion file executed successfully.")
    obj = DataIngestion()
    train, test = obj.initiate_data_ingestion()
    print("Train shape:", train.shape)
    print("Test shape:", test.shape)




