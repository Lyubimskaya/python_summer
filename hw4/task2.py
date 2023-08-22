"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""

def dict_key(**kwargs):
    res = {}
    for key, value in kwargs.items():
        try:
            res[value] = key
        except TypeError:
            res[str(value)] = key
    return res


print(dict_key(a=100, b=15, c=38, d=6, e=1))