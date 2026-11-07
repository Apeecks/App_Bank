import datetime
from typing import Optional

import pandas as pd


def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    """
    Выводит средние траты по дням недели за последние три месяца от указанной даты(если не указанна берется текущая)
    """
    if date is None:
        date = datetime.date.today().strftime("%d.%m.%Y")

    split_date = date.split(".")
    date_obj = datetime.datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))
    list_date = []
    for x in transactions.get("Дата платежа"):
        try:
            split_x = x.split(".")
            date_odj_df = datetime.datetime(int(split_x[2]), int(split_x[1]), int(split_x[0]))
            if (
                date_odj_df <= date_obj
                and date_odj_df.month >= date_obj.month - 2
                and date_odj_df.year == date_obj.year
            ):
                list_date.append(x)
        except AttributeError:
            continue

    df = transactions.loc[transactions["Дата платежа"].isin(list_date)]

    sum_dict = {"Пн": 0, "Вт": 0, "Ср": 0, "Чт": 0, "Пт": 0, "Сб": 0, "Вс": 0}
    sum_iter = {"Пн": 0, "Вт": 0, "Ср": 0, "Чт": 0, "Пт": 0, "Сб": 0, "Вс": 0}

    for i, row in df.iterrows():
        date_row = df["Дата платежа"][i].split(".")
        date_x_obj = datetime.datetime(int(date_row[2]), int(date_row[1]), int(date_row[0]))
        dict_weak = {"0": "Вс", "1": "Пн", "2": "Вт", "3": "Ср", "4": "Чт", "5": "Пт", "6": "Сб"}
        weekday = date_x_obj.strftime("%w")
        if int(df["Сумма операции"][i]) < 0:
            sum_dict[dict_weak.get(weekday)] = sum_dict.get(dict_weak.get(weekday)) + int(df["Сумма операции"][i])
            sum_iter[dict_weak.get(weekday)] = sum_iter.get(dict_weak.get(weekday)) + 1

    result = {}
    for key, x in sum_dict.items():
        try:
            result[key] = int(abs(x / sum_iter.get(key)))
        except ZeroDivisionError:
            result[key] = 0

    result_df = pd.DataFrame(result, index=[0])
    return result_df
