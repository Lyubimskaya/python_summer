"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

frac1 = input("Введите первую дробь вида a/b: ")
frac2 = input("Введите вторую дробь вида a/b: ")

num1, den1 = map(int, frac1.split("/"))
num2, den2 = map(int, frac2.split("/"))

f1 = Fraction(num1, den1)
f2 = Fraction(num2, den2)
print(f"Проверка модулем Fraction: сумма {f1 + f2}, произведение {f1 * f2}")

if den1 != den2:
    num_sum = num1 * den2 + num2 * den1
    den_sum = den1 * den2
else:
    num_sum = num1 + num2
    den_sum = den1

num_prod = num1 * num2
den_prod = den1 * den2

print(f"Сумма: {num_sum}/{den_sum}")
print(f"Произведение: {num_prod}/{den_prod}")