import json

from src.services import search_json
from src.utils import read_json


def test_search_json():
    transactions = [
        {
            "Описание": "Перевод другу",
            "Категория": "Переводы"
        },
        {
            "Описание": "Покупка хлеба",
            "Категория": "Супермаркеты"
        }
    ]
    result = search_json(transactions, "перевод")
    expected = [transactions[0]]
    assert json.loads(result) == expected
    assert read_json("data/services.json") == expected
