from fastapi import APIRouter
from model_train import IrisClassifier, IrisSpecies
from starlette.responses import JSONResponse

router = APIRouter()

@router.post('/classify_iris')
def extract_name(iris: IrisSpecies):
    iris_features = iris.dict()
    iris_classifier = IrisClassifier()
    return JSONResponse(iris_classifier.classify_iris(iris_features))