import csv
import json
from typing import Any

import pandas as pd


def read_file_xlsx(path: str) -> Any:
    """Принимает файл xlsx, возвращает список словарей"""
    try:
        df = pd.read_excel(path)
        df_dict = df.ffill().to_dict(orient="records")
        return df_dict
    except FileNotFoundError:
        print("Файл не найден")
        return []


def read_file_csv(path: str) -> list:
    """Принимает файл csv, возвращает список словарей"""
    try:
        with open(path) as f:
            reader = csv.DictReader(f)
            list_dict = []
            for row in reader:
                list_dict.append(row)
        return list_dict
    except FileNotFoundError:
        print("Файл не найден")
        return []


def writer_file_json(path: str, info: Any) -> Any:
    """
    Записывает переданную info в json файл
    """
    try:
        with open(path, "w") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        return "Файл не найден"


def read_json(path: str) -> Any:
    """
    Читает json файл
    """
    try:
        with open(path) as f:
            result = json.load(f)
        return result
    except FileNotFoundError:
        return "Файл не найден"


def read_xlsx_return_df(path: str) -> Any:
    """
    Читает xlxs файл возвращает pd.DataFrame
    """
    try:
        df = pd.read_excel(path)
        return df
    except FileNotFoundError:
        print("Файл не найден")
        return []


def writer_txt(path: str, info: str) -> Any:
    """
    Записывает переданную info в переданный путь
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{info}\n")