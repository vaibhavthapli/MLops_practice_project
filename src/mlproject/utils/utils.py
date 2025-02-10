import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd

from dotenv import load_dotenv
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score
import pymysql

import pickle
import numpy as np

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established", mydb)
        df = pd.read_sql_query('Select * from students', mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param, n_iter=10, cv=3):
    try:
        report = {}

        for model_name, model in models.items():
            print(f"Evaluating Model: {model_name}")

            para = param.get(model_name, {})

            if not hasattr(model, "fit"):
                raise CustomException(f"Model {model_name} does not support fitting.", sys)

            if len(para) > 0:
                n_iter_actual = min(n_iter, len(para))
                rs = RandomizedSearchCV(
                    estimator=model,
                    param_distributions=para,
                    n_iter=n_iter_actual,
                    cv=cv,
                    scoring='r2',
                    n_jobs=-1,
                    random_state=42
                )
                rs.fit(X_train, y_train)

                if hasattr(model, "set_params"):
                    model.set_params(**rs.best_params_)
                else:
                    raise CustomException(f"Model {model_name} does not support set_params.", sys)

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)