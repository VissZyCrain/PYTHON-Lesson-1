# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек 
# в этой четверти (x и y)

import os
os.system('cls')

print('Задача № 3')

n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
     print('Ошибка! Пожалуйста, измените ввод номера четверти!')
elif n == 1: print('Возможный диапозон координат точек: x от 0 до + ∞, y от 0 до + ∞')
elif n == 2: print('Возможный диапозон координат точек: x от 0 до - ∞, y от 0 до + ∞')
elif n == 3: print('Возможный диапозон координат точек: x от 0 до - ∞, y от 0 до - ∞')
elif n == 4: print('Возможный диапозон координат точек: x от 0 до + ∞, y от 0 до - ∞')