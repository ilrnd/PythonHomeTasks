# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя 
# и Сережа сделали одинаковое количество журавликов,а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
import os
os.system('clear')
s = int(input('Введите количество журавликов: '))
while (s < 6 or s % 2 != 0):
    s = int(input('Введите корректное количество журавликов: '))
print(f'Петя сделал - {int(s / 6)}, Катя - {int(4 * s / 6)}, Сережа - {int(s / 6)} журавликов')