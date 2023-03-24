# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
import os
os.system('clear')
def sum_number(a, b):
    if a == 0: 
       return b
    return sum_number(a - 1, b + 1)
a, b = int(input('Введите число a: ')), int(input('Введите число b: '))
print(sum_number(a, b))