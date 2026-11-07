import os
from typing import Any

from src.review_file import date_overview, new_sort_file_csv, review_file_operations


def test_date_overview(test_date_overview_m: list) -> Any:
    """
    Как смог ;(
    """
    assert date_overview("01.01.2018") == test_date_overview_m
    assert date_overview("01.01.2018", "W") == test_date_overview_m
    assert date_overview("01.01.2018", "Y") == test_date_overview_m
    assert date_overview("01.01.2018", "ALL") == test_date_overview_m


def test_review_file_operations(result_review: dict) -> Any:
    """
    Проверка работы функций в модуле review_file
    """
    dict_ = review_file_operations(new_sort_file_csv("01.01.2018"))

    assert dict_ == result_review

    os.remove("result.csv")