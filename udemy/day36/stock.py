# TODO - make a stock price tracker and send price updates of stock price daily
import requests
import json

def pullstock(x):
    stock_param={
        "function":"TIME_SERIES_DAILY",
        "symbol":x,
        "apikey":"QQA7NEVR47LPP4NK"
    }
    with open(f"{x}.json","w") as file:
        stock=requests.get(url="https://www.alphavantage.co/query",params=stock_param)
        json.dump(stock.json(),file,indent=4)
        file.close()
        return stock.json()
print(pullstock("GOOGL"))