import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()


API_KEY = os.getenv("API_KEY")

headers = {'X-CMC_PRO_API_KEY': API_KEY }

base_url = "https://pro-api.coinmarketcap.com"

trending_Url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"



request = requests.get(trending_Url,headers=headers)





def getQuote(name):
    crypto_info = f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?slug={name}" 
    request = requests.get(crypto_info,headers=headers)
    result = request.json()
    data =  result["data"]
    for item in data:
       cryptoID = item
    cryptoData = result["data"][f"{cryptoID}"]  
    for key,value in  cryptoData.items():
        print(key,value)
    print(cryptoData["description"])
    print("social handle is :" " " "@" + cryptoData["twitter_username"])
       


 

crypto = input("crypto name:")

getQuote(crypto)

