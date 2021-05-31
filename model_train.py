import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib
from pydantic import BaseModel

class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float


class IrisClassifier:
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        self.iris_type = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }
        self.model_fname_ = "iris_model.pkl"

        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self.train_model()
            joblib.dump(self.model, self.model_fname_)
        

    def train_model(self) -> LogisticRegression:
        return LogisticRegression(solver='lbfgs',
                                  max_iter=1000,
                                  multi_class='multinomial').fit(self.X, self.y)

    def classify_iris(self, features: dict):
        X = [features['sepal_length'], features['sepal_width'], features['petal_length'], features['petal_width']]
        prediction = self.model.predict_proba([X])
        return {'class': self.iris_type[np.argmax(prediction)],
                'probability': round(max(prediction[0]), 2)}