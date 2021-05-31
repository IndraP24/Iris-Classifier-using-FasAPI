# 1. Library Imports
import uvicorn
from fastapi import FastAPI

# 2. Create FastAPI app object
app = FastAPI()

# 3. Index route to open on localhost automatically
@app.get('/')
def index():
    '''
    This is an initial docstring. It is the default page that loads.
    '''
    return {'message': 'Hello, Stranger'}


# 4. Route with a single parameter, returns the parameter within a message

@app.get('/{name}')
def get_name(name: str):
    '''
    This is the second docstring. It loads when a parameter is provided.
    '''
    return {'message': f'Hello, {name}'}


# 5. Run the API with uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)