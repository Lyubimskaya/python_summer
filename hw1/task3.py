"""
3. Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

number = int(input("Введите число от 0 до 100000: "))
count = 0

if number < 0 or number > 100000:
    print("Введенное число некорректно")
elif number == 0 or number == 1:
    print(f"Число {number} не является простым или составным")
else:
    for i in range(2, number + 1):
        if number % i == 0:
            count += 1
    if count == 1:
        print(f"Число {number} является простым")
    else:
        print(f"Число {number} является составным")