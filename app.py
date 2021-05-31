from fastapi import FastAPI
from router import iris_router

app = FastAPI()
app.include_router(iris_router.router, prefix='/iris')


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'