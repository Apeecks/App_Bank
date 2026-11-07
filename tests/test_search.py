from src.search import search_file_xlsx


def test_search_description():
    transactions = [
        {"Описание": "Перевод другу", "Категория": "Переводы"},
        {"Описание": "Покупка продуктов", "Категория": "Супермаркеты"},
    ]
    result = search_file_xlsx(transactions, "пеРЕвод")
    assert result == [transactions[0]]


def test_search_category():
    transactions = [
        {"Описание": "Оплата", "Категория": "Транспорт"},
        {"Описание": "Покупка", "Категория": "Аптеки"},
    ]
    result = search_file_xlsx(transactions, "аптеки")
    assert result == [transactions[1]]


def test_search_ignores_other_fields():
    transactions = [
        {
            "Описание": "Оплата",
            "Категория": "Супермаркеты",
            "Комментарий": "Перевод",
        }
    ]
    assert search_file_xlsx(transactions, "перевод") == []