'''Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. 
билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no'''

ticket = str (input('Введите номер билета из 6 цифр:'))
if len(ticket)==6:
    num1=int (ticket[0])
    num2=int (ticket[1])
    num3=int (ticket[2])
    num4=int (ticket[3])
    num5=int (ticket[4])
    num6=int (ticket[5])
    if num1+num2+num3==num4+num5+num6:
        print(f"Билет {ticket} счастливый")
    else:
        print(f"Билет {ticket} не счастливый")
else:
    print("Введите корректное число")