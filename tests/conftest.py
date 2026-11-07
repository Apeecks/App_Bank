import pandas as pd
import pytest


@pytest.fixture
def test_list_dict_def_read_csv() -> list:
    return [
        {"titel1": "1", "title2": "4", "title3": "7"},
        {"titel1": "2", "title2": "5", "title3": "8"},
        {"titel1": "3", "title2": "6", "title3": "9"},
    ]


@pytest.fixture
def test_list_dict_def_read_csv_result() -> list:
    return [
        {"titel1": 1, "title2": 4, "title3": 7},
        {"titel1": 2, "title2": 5, "title3": 8},
        {"titel1": 3, "title2": 6, "title3": 9},
    ]


@pytest.fixture
def test_date_overview_m() -> list:
    return [
        {
            "Дата операции": "01.01.2018 12:49:53",
            "Дата платежа": "01.01.2018",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -3000.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -3000.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 15.0,
            "Категория": "Переводы",
            "MCC": 5977.0,
            "Описание": "Линзомат ТЦ Юность",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 3000.0,
        }
    ]


@pytest.fixture
def result_review() -> dict:
    return {
        "expenses": {"total_amount": 3000, "main": [{"category": "other", "amount": 0}]},
        "transfers_and_cash": [{"category": "Переводы", "amount": 3000}],
        "income": {"total_amount": 0, "main": []},
    }


@pytest.fixture
def test_search_list_dict() -> list:
    return [{"1": "one"}, {"2": "two"}]


@pytest.fixture
def test_transactions_spending_by_weekday() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Дата платежа": ["31.03.2025", "01.04.2025", "02.04.2025", "03.04.2025", "06.04.2025", "07.04.2025"],
            "Сумма операции": [-100, -100, -100, -100, -100, -200],
        }
    )
