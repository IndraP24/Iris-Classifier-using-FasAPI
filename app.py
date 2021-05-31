from fastapi import FastAPI
from router import iris_router
import uvicorn

app = FastAPI()
app.include_router(iris_router.router, prefix='/iris')


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)