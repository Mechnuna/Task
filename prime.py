__all__ = (
    'is_prime',
)


import re


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number == 1:
        return False
    d = 2
    while number % d != 0:
        d += 1
    return d == number

print(is_prime(1))