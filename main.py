from fastapi import FastAPI

app = FastAPI()

@app.get('/predict')
def root(a: int, b: int, c: int):
    return {'message': a+b+c}