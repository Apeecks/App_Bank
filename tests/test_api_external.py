import os
from typing import Any
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

from src.api_external import currency, stocks


@patch("requests.get")
def test_currency(mock_get: MagicMock) -> Any:
    """
    Тест получение курса валют
    """
    load_dotenv()
    apilayer_key = os.getenv("APILayer_KEY")
    params = f"https://api.apilayer.com/exchangerates_data/convert?amount=100&from=EUR&to=RUB&apikey={apilayer_key}"

    mock_get.return_value.json.return_value = {"info": {"rate": 80}}
    assert currency() == {"currency_rates": [{"currency": "USD", "rate": 80}, {"currency": "EUR", "rate": 80}]}
    mock_get.assert_called_with(params)


@patch("requests.get")
def test_stocks(mock_get: MagicMock) -> Any:
    """
    Тест получение котировок акций
    """
    load_dotenv()
    apikey = os.getenv("APIAlpha_Vantage_KEY")
    test_list = ["MSFT", "AAPL", "IBM"]
    url = "https://www.alphavantage.co/query"
    params = {"function": "REALTIME_BULK_QUOTES", "symbol": test_list, "apikey": apikey}

    mock_get.return_value.json.return_value = {
        "data": [{"symbol": "MSFT", "open": "1"}, {"symbol": "AAPL", "open": "2"}, {"symbol": "IBM", "open": "3"}]
    }
    assert stocks() == {
        "stock_prices": [
            {"stock": "MSFT", "price": "1"},
            {"stock": "AAPL", "price": "2"},
            {"stock": "IBM", "price": "3"},
        ]
    }
    mock_get.assert_called_once_with(url, params=params)
