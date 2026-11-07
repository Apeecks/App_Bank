import os

from src.api_external import currency, stocks
from src.review_file import new_sort_file_csv, review_file_operations
from src.utils import writer_file_json


def review_date_operations(date: str, span: str = "M") -> str:
    """Складывание функций, получение json файла-ответа"""
    file_csv = new_sort_file_csv(date, span)
    json_file = review_file_operations(file_csv)

    dict_currency = currency()
    dict_stocks = stocks()
    json_file.update(dict_currency)
    json_file.update(dict_stocks)

    writer_file_json("data/result.json", json_file)
    os.remove(file_csv)
    return "Файл result.json успешно создан"