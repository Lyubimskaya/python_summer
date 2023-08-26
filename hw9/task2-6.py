"""Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""

import csv
import json
import random
import math
import functools


# 2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def file_csv(file_csv):
    with open(file_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(random.randint(100, 1001)):
            writer.writerow([random.randint(0, 101) for _ in range(3)])


# 3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def dec_roots(func):
    @functools.wraps(func)
    def wrapper(filename):
        res = []
        with open(filename, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                res.append(func(a, b, c))
        return res

    return wrapper


# 4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
def dec_res(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('log.json', 'a') as f:
            json.dump({'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': res}, f)
        return res

    return wrapper

@dec_roots
@dec_res
# 1. функция нахождения корней квадратного уравнения
def roots_quad(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a != 0:
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            print(f"x1 = {x1} \nx2 = {x2}")
        elif discr == 0:
            x = -b / (2 * a)
            print(f"x1 = x2 = {x}")
        else:
            print("Корней нет")

    else:
        print("Уравнение не является квадратным")


file_csv('multipliers.csv')
roots_quad('multipliers.csv')
