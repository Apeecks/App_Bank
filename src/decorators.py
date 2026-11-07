from functools import wraps
from typing import Any

from src.utils import writer_txt


def result_func(filename: str = "data/reports_result.txt") -> Any:
    """
    Записывает в файл результат функции
    """

    def function(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            writer_txt(filename, f"Результат функции {func.__name__}: {result}")
            return "success"

        return wrapper

    return function
