def search_file_xlsx(list_dict: list, search_str: str) -> list:
    """
    Поиск транзакций по описанию или категории без учёта регистра.
    """
    sort_list = []
    search_str = search_str.lower()

    for x in list_dict:
        description = str(x.get("Описание", "")).lower()
        category = str(x.get("Категория", "")).lower()

        if search_str in description or search_str in category:
            sort_list.append(x)

    return sort_list