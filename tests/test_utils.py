import csv
import os
from typing import Any

import pandas as pd

from src.utils import read_file_csv, read_file_xlsx, read_json, writer_file_json


def test_read_file_csv_xlsx(test_list_dict_def_read_csv: dict, test_list_dict_def_read_csv_result: dict) -> Any:
    """
    Проверка правильности чтения файла csv
    """
    with open("test.csv", "w", newline="", encoding="utf-8") as f:
        header = ["titel1", "title2", "title3"]
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        for row in test_list_dict_def_read_csv:
            writer.writerow(row)

    df = pd.read_csv("test.csv")
    df.to_excel("test.xlsx", index=False)

    assert read_file_csv("test.csv") == test_list_dict_def_read_csv
    assert read_file_xlsx("test.xlsx") == test_list_dict_def_read_csv_result

    assert read_file_csv("") == []
    assert read_file_xlsx("") == []

    os.remove("test.csv")
    os.remove("test.xlsx")


def test_read_write_json() -> Any:
    """
    Проверка правильности чтения json файла
    """
    info: dict = {"test": "one"}

    assert writer_file_json("", info) == "Файл не найден"

    writer_file_json("test.json", info)

    assert read_json("test.json") == info
    assert read_json("") == "Файл не найден"

    os.remove("test.json")
