import pandas as pd
import joblib
import sys
import os
from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        self.pipeline_path = os.path.join("artifacts", "pipeline.pkl")

    def predict(self, features: pd.DataFrame):
        try:
            pipeline = joblib.load(self.pipeline_path)
            return pipeline.predict(features)
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 gender,
                 race_ethnicity,
                 parental_level_of_education,
                 lunch,
                 test_preparation_course,
                 reading_score,
                 writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            data_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score]
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            raise CustomException(e, sys)
