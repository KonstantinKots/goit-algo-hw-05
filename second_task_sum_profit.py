
import re
from typing import Callable, Iterator
#Функція для аналізу сторки на наявність чисел
def generator_numbers(text: str):
    """Генератор чисел з тексту.
    Ловить числа з крапкою"""
    for num in re.findall(r" \d+\.\d+ ", text):
        yield float(num)

#Функція обрахування загального прибутку
def sum_profit(text: str, func: Callable [[str], Iterator[float]]) -> float:
    """Обчислює суму чисел, які повертає функція func."""
    return sum(func(text))

def main():
    text = """Загальний дохід працівника складається з декількох
     частин: 1000.01 як основний дохід, доповнений додатковими
     надходженнями 27.45 і 324.00 доларів."""
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")

if __name__ == '__main__':
    main()
