"""
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

import cmath
import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

discr = b ** 2 - 4 * a * c
print("Дискриминант =", discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x1 = x2 = {x}")
else:
    x1 = (-b + cmath.sqrt(discr)) / (2 * a)
    x2 = (-b - cmath.sqrt(discr)) / (2 * a)

    print(f"Комплексные корни: \nx1 = {x1} \nx2 = {x2}")
