# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
os.system('cls')

print('Задача № 1')
number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели неверное число! Попробуйте еще раз!')
elif number > 5:
    print('Да, этот день выходной!')
else:
    print('Нет, это рабочий день!')