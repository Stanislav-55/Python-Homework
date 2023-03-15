'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |'''

number = str(input("Введите 3-х значное число:"))
numberA = int(number[0])
numberB = int(number[1])
numberC = int(number[2])
print(f"Сумма трех чисел равна {numberA+numberB+numberC}")