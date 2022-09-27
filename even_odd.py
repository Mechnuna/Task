__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    c, n = 0, 0
    for i in arr:
        if i % 2 == 0:
            c += i
        else:
            n += i
    if n:
        return c/n 
    return 0
