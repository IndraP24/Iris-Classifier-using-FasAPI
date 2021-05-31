import pandas as pd
from pandas.core.algorithms import mode
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from pydantic import BaseModel
import joblib


class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float 
    petal_width: float


class IrisModel:
    def __init__(self):
        self.iris = load_iris()
        self.X = self.iris.data
        self.y = self.iris.target

        self.model_fname_ = "iris_model.pkl"

        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)


    def _train_model(self):
        X = self.X
        y = self.y
        rf = RandomForestClassifier()
        model = rf.fit(X, y)
        return model


    def predict_species(self, epal_length, sepal_width, petal_length, petal_width):
        data_in = [[epal_length, sepal_width, petal_length, petal_width]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability
