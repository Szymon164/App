from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root(a: int):
    return {'message': a}