"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла"""

import os


def full_path(file_path):
    return os.path.split(file_path)[0], *os.path.split(file_path)[-1].split('.')


print(full_path('C:\Images\new\photo_2022-11-21_15-51-01.jpg'))
