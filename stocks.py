import requests
import os
def get_stocks():
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"function":"TIME_SERIES_DAILY","symbol":"MSFT","outputsize":"compact","datatype":"json"}

    headers = {
        "X-RapidAPI-Key": os.environ('RAPID-API-KEY'),
        "X-RapidAPI-Host": os.environ('RAPID-API-HOST')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()