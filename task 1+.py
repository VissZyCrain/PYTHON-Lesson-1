# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) =
#  ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

import os
os.system('cls')

print('Задача № 1 доп')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истенно при x = {x}, y={y}, z={z}')
