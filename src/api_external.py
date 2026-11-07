import os

import requests
from dotenv import load_dotenv

from src.utils import read_json


def currency() -> dict:
    """Получение курса валют, возврат словаря"""
    result = {}
    load_dotenv()
    apilayer_key = os.getenv("APILayer_KEY")
    url_usd = f"https://api.apilayer.com/exchangerates_data/convert?amount=100&from=USD&to=RUB&apikey={apilayer_key}"
    url_eur = f"https://api.apilayer.com/exchangerates_data/convert?amount=100&from=EUR&to=RUB&apikey={apilayer_key}"
    result_usd = requests.get(url_usd).json()
    result_eur = requests.get(url_eur).json()
    result["currency_rates"] = [
        {"currency": "USD", "rate": result_usd["info"]["rate"]},
        {"currency": "EUR", "rate": result_eur["info"]["rate"]},
    ]
    return result


def stocks() -> dict:
    """Получение курса акций, возврат словаря"""
    user_setting = read_json("data/user_settings.json")
    list_stocks = user_setting.get("user_stocks")
    load_dotenv()
    result = {}
    apilayer_key = os.getenv("APIAlpha_Vantage_KEY")
    url = "https://www.alphavantage.co/query"
    params = {"function": "REALTIME_BULK_QUOTES", "symbol": list_stocks, "apikey": apilayer_key}
    result_requests = requests.get(url, params=params).json()
    result["stock_prices"] = [{"stock": x["symbol"], "price": x["open"]} for x in result_requests.get("data")]
    return result