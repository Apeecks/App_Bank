import pandas as pd

from src.date_sort import spending_by_weekday


def test_spending_by_weekday(test_transactions_spending_by_weekday):

    expected = pd.DataFrame({
        "Пн": [150],
        "Вт": [100],
        "Ср": [100],
        "Чт": [100],
        "Пт": [0],
        "Сб": [0],
        "Вс": [100]
    })
    result = spending_by_weekday(test_transactions_spending_by_weekday,"07.04.2025")
    assert result.equals(expected)
