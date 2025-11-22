import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from src.utils import save_object, evaluate_models
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        """
        Train multiple regression models, evaluate, save best model.
        Args:
            train_array (np.array): training data
            test_array (np.array): test data
        Returns:
            dict: evaluation report (r2 scores)
        """
        try:
            logging.info("Splitting training and test data...")

            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            logging.info("Defining models for training...")
            models = {
                "LinearRegression": LinearRegression(),
                "DecisionTree": DecisionTreeRegressor(),
                "RandomForest": RandomForestRegressor()
            }

            logging.info("Evaluating models...")
            model_report = evaluate_models(X_train, y_train, X_test, y_test, models)

            logging.info(f"Model evaluation report: {model_report}")

            # Select best model
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]

            logging.info(f"Best model found: {best_model_name} with R2 score {model_report[best_model_name]}")

            # Fit best model on full training data before saving
            best_model.fit(X_train, y_train)

            # Save the trained model
            save_object(self.model_trainer_config.trained_model_file_path, best_model)
            logging.info(f"Trained model saved at {self.model_trainer_config.trained_model_file_path}")

            return model_report

        except Exception as e:
            raise CustomException(e, sys)


# For testing as standalone script
if __name__ == "__main__":
    from src.components.data_ingestion import DataIngestion

    try:
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        trainer = ModelTrainer()
        report = trainer.initiate_model_trainer(train_data, test_data)

        print("Model training and evaluation completed!")
        print(report)

    except Exception as e:
        print(e)
