import pandas
from fastapi import FastAPI
from stocks import get_stocks

app = FastAPI()

@app.get('/')
def root():
    tmp = get_stocks()
    return tmp

