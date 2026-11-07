import os
from typing import Any

from src.decorators import result_func


def test_decorators() -> Any:
    """
    Тестирование записи результата рабаты ф-ии в файл
    """

    @result_func("test")
    def test_func() -> int:
        return 20

    test_func()
    with open("test", "r", encoding="utf-8") as f:
        str_result = f.readline()
    assert str_result == "Результат функции test_func: 20\n"

    os.remove("test")
