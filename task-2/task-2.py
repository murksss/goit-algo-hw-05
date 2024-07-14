from typing import Callable, Iterator
import re


def generator_numbers(_text: str) -> Iterator[int]:
    numbers = re.findall(r'\d+\.\d+', _text)
    for number in numbers:
        yield float(number)


def sum_profit(_text: str, func: Callable) -> float:
    return sum(func(_text))


if __name__ == '__main__':
    text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як "
            "основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
