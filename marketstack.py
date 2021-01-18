
#access key 
marketstack = "e4a4f96789c854d8690960f5ff1dd666"

#0 explore the marketstack docs and find the relevant url
#1 integrate api


#imports
import requests
import json

api_key = marketstack

base_url = "http://api.marketstack.com/v1/"

def get_stock_price(stock_symbol):
    dict1 = {"access_key": api_key}
    end_point = ''.join([base_url,"tickers/",stock_symbol,"/intraday/latest"])
    api_result = requests.get(end_point,dict1)
    json_result = json.loads(api_result.text)
    return {
        "Price_Details": json_result
    }


