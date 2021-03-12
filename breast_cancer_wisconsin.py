import routes
import uvicorn
from typing import List
import json
from fastapi import FastAPI
from prediction import predictions_

app = FastAPI()


@app.get('/')
def index():
    return {'mensaje': 'Hola, extraño'}


@app.get(routes.HELLO)
def welcome():
    return {'message': 'Hola Francisco, esta es nuestra primera API'}


@app.get(routes.ECO)
def eco(mirror: str):
    return {'message': f'eco: {mirror}'}


@app.post(routes.PREDICTION)
def prediction(data):
    result = predictions_(patient=json.loads(data))

    return 'El paciente tiene Cancer' if result==4 else 'El paciente esta sano'


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
