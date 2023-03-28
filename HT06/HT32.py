# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import os, random
os.system('clear')
def fill_array(n):
    list_1 = [random.randint(-10, 20) for i in range(n)]
    return list_1

def find_index(list_1, start, stop):
    list_out = []
    for i in range(len(list_1)):
        if start <= list_1[i] <= stop:
            list_out.append(i)
    return list_out

n = int(input('Введите количество элементов массива N: '))
list_in = fill_array(n)
print(list_in)
a, b = int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))
print(find_index(list_in, a, b))