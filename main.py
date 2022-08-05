from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'code': 200}

@app.get('/predict')
def predict(a: int, b: int, c: int):
    return {'message': a+b+c}