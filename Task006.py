# 6. Описание числа
# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "ноль",
# "положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число".

num = int(input('Введите целое число :'))
if num > 0 and num % 2 == 0:
    print("положительное четное число")
elif num > 0 and num % 2 != 0:
    print("положительное не четное число")
elif num==0:
    print("ноль")
elif num < 0 and num % 2 == 0:
    print("отрицательное четное число")
elif num < 0 and num % 2 != 0:
    print("отрицательное не четное число")
