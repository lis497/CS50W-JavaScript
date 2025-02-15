import json
import requests
from pprint import pprint

# easy way
#url = "https://api.apilayer.com/exchangerates_data/latest?base=USD&apikey=wpnGQL0okI2o4fj9CCASS50JxWU33xgb"
#data = requests.get(url).json()

url = "https://api.apilayer.com/exchangerates_data/latest"
param = {"base": "USD",
         "apikey":"wpnGQL0okI2o4fj9CCASS50JxWU33xgb"}

data = requests.get(url, param).json()

pprint(data)