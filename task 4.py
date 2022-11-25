# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
os.system('cls')

print('Задача № 4')

ax = float(input('Введите координаты точки A по оси х:'))
ay = float(input('Введите координаты точки A по оси y:'))
bx = float(input('Введите координаты точки B по оси x:'))
by = float(input('Введите координаты точки B по оси y:'))

import math
distance = math.sqrt ((ax - bx)**2 + (ay - by)**2)
distance = int(distance * 100)
distance = float(distance/100)
print(f'Растояние между точкой A до точки B = {distance}' )