import csv
import logging
import os
from typing import Any

from src.utils import read_file_csv, read_file_xlsx

logger = logging.getLogger("review_file")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/review_file.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def date_overview(date: str, span: str = "M") -> list:
    """Читает excel файл, сортирует по заданной дате и интервалу-span. Возвращает csv файл"""
    list_dict = read_file_xlsx("data/operations.xlsx")
    list_date = date.split(".")
    if span == "W":
        results = [
            x
            for x in list_dict
            if str(x.get("Дата платежа")) != ""
            if str(x.get("Дата платежа")).split(".")[1] == list_date[1]
            if str(x.get("Дата платежа")).split(".")[2] == list_date[2]
            if list_date[0] >= str(x.get("Дата платежа")).split(".")[0] >= str(int(list_date[0]) - 7)
        ]
    elif span == "Y":
        results = [
            x
            for x in list_dict
            if str(x.get("Дата платежа")) != ""
            if str(x.get("Дата платежа")).split(".")[2] == list_date[2]
            if str(x.get("Дата платежа")).split(".")[0] <= list_date[0]
            if str(x.get("Дата платежа")).split(".")[1] <= list_date[1]
        ]
    elif span == "ALL":
        results = [
            x
            for x in list_dict
            if str(x.get("Дата платежа")) != ""
            if str(x.get("Дата платежа")).split(".")[1] <= list_date[1]
            if str(x.get("Дата платежа")).split(".")[2] <= list_date[2]
            if str(x.get("Дата платежа")).split(".")[0] <= list_date[0]
        ]
    else:
        results = [
            x
            for x in list_dict
            if str(x.get("Дата платежа")) != ""
            if str(x.get("Дата платежа")).split(".")[1] == list_date[1]
            if str(x.get("Дата платежа")).split(".")[2] == list_date[2]
            if str(x.get("Дата платежа")).split(".")[0] <= list_date[0]
        ]
    return results


def new_sort_file_csv(date: str, span: str = "M") -> Any:
    """
    Создает файл csv
    """
    results = date_overview(date, span)
    with open("result.csv", "w", newline="") as f:
        fieldnames = [
            "Дата операции",
            "Дата платежа",
            "Номер карты",
            "Статус",
            "Сумма операции",
            "Валюта операции",
            "Сумма платежа",
            "Валюта платежа",
            "Кэшбэк",
            "Категория",
            "MCC",
            "Описание",
            "Бонусы (включая кэшбэк)",
            "Округление на инвесткопилку",
            "Сумма операции с округлением",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    return os.path.abspath("result.csv")


def review_file_operations(path_to_file: str) -> dict:
    """
    Анализ файла csv, вывод словаря
    """
    logger.info("Чтение файла")
    list_dict = read_file_csv(path_to_file)
    logger.info("Подсчет суммы трат и сумму поступлений")
    sum_expenses = 0.0
    sum_profit = 0.0
    for x in list_dict:
        if x.get("Сумма операции") < "0":
            sum_expenses += float(x.get("Сумма операции"))
        else:
            sum_profit += float(x.get("Сумма операции"))
    logger.info('Создание и сортировка списка кортежей: [("Категория", "Сумма")...]')
    dict_category: dict = {}
    for x in list_dict:
        if x.get("Категория") in dict_category.keys():
            dict_category[x.get("Категория")] = float(x.get("Сумма платежа")) + float(
                dict_category.get(x.get("Категория"))
            )
        else:
            dict_category[x.get("Категория")] = float(x.get("Сумма платежа"))
    sort_list = sorted(dict_category.items(), key=lambda x: x[1])

    logger.info("Сортировка списка кортежей по группам")
    category_top = []
    category_nal = []
    category_profit = []
    sum_x = 0.0
    for x in sort_list:
        if x[0] not in ["Переводы", "Наличные"] and x[1] < 0:
            if sort_list.index(x) <= 7:
                category_top.append(x)
            else:
                sum_x += float(x[1])
        elif x[0] in ["Переводы", "Наличные"]:
            category_nal.append(x)
        else:
            category_profit.append(x)
    category_top.append(("other", sum_x))
    logger.info("Создание файла json")
    result_review_file = {
        "expenses": {
            "total_amount": abs(round(sum_expenses)),
            "main": [{"category": x[0], "amount": abs(round(x[1]))} for x in category_top],
        },
        "transfers_and_cash": [{"category": x[0], "amount": abs(round(x[1]))} for x in category_nal],
        "income": {
            "total_amount": round(sum_profit),
            "main": [{"category": x[0], "amount": abs(round(x[1]))} for x in category_profit],
        },
    }
    return result_review_file