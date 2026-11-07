import json

import pandas as pd

from src.search import search_file_xlsx
from src.utils import writer_file_json


def search_json(list_dict: list, search_str: str) -> str:
    """
    Поиск транзакций и возврат результата в формате JSON.
    """
    result = search_file_xlsx(list_dict, search_str)
    json_result = pd.DataFrame(result).to_json(orient="records", force_ascii=False)
    writer_file_json("data/services.json", json.loads(json_result))
    return json_result
