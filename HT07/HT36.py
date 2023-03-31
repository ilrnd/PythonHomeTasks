# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
import os
os.system('clear')

def print_operation_table(operation, num_rows=6, num_columns=6):
    list_1 = [[operation(i + 1, j + 1) for j in range(num_columns)] for i in range(num_rows)]
    x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in list_1])
    print(x)
print_operation_table(lambda x, y: x * y)
