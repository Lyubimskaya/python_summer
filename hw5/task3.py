"""
Создайте функцию генератор чисел Фибоначчи
"""

import itertools


def list_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(itertools.islice(list_fib(), 20))) # Генерация первых 20 чисел