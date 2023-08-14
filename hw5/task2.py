"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии"""

names = ['Sasha', 'Masha', 'Pasha']
wage = [30000, 25000, 36000]
bonus = ["10.25%", "11.50%", "11.25%"]

new_dict = {item[0]: item[1] * float(item[2][:-1]) / 100 for item in zip(names, wage, bonus)}

print(new_dict)