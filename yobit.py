import hmac
import hashlib
import requests
from time import time
from os import getenv
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv('.env')
key = getenv("API_KEY")
secret = getenv("API_SECRET")


def get_info():
    values = dict()
    values["method"] = "getInfo"
    values["nonce"] = str(int(time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(secret.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {"key": key, "sign": sign}
    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)

    return response.json()


def get_deposit_address(coin_name="btc"):
    values = dict()
    values["method"] = "GetDepositAddress"
    values["coinName"] = coin_name
    values["need_new"] = 0
    values["nonce"] = str(int(time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(secret.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {"key": key, "sign": sign}
    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)

    return response.json()

# get_info()
# coin = input("Enter a coin name: ")
# print(f'Address: {get_deposit_address(coin_name=coin)}')
