# Задача 26: Напишите программу, 
# которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.\
import os
os.system('clear')
def degree(x, y):
    if y == 0:
        return 1
    return x * degree(x, y - 1)
a, b = int(input('Введите число A: ')), int(input('Введите число B: '))
print(f'{a} в степени {b} = {degree(a, b)}')
