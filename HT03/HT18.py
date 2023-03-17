# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
import os
from random import randint
import math
os.system('clear')
n = int(input('Введите число N: '))
x = int(input('Введите искомое число X: '))
lst = [randint(1, 10) for i in range(n)]
print(lst)
min = abs(x - lst[0])
index = 0
for i in range(1, n):
    if abs(x - lst[i]) < min:
        min = abs(x - lst[i])
        index = i
print(f'Самый близкий элемент к {x} = {lst[index]}')        