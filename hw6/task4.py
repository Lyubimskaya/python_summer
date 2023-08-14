"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

import random
from task3 import ranking_queens


def queens_positions():
    positions = list(range(1, 9))
    for i in range(4):
        random.shuffle(positions)
        while not ranking_queens(positions):
            random.shuffle(positions)
        dct = {el: positions[el - 1] for el in positions}
        print(f"{sorted(dct.items())} - успешная расстановка {i + 1}")


queens_positions()