# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# i ягод.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло a
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import os
os.system('clear')
import random
n = int(input('Введите число грядок N: '))
bushes = [random.randint(5, 15) for i in range(n)]
print(bushes)
max = bushes[n - 1] + bushes[n - 2] + bushes[0]
if bushes[n - 1] + bushes[0] + bushes[1] > max:
    max = bushes[n - 1] + bushes[0] + bushes[1]
for i in range(1, n - 1):
    if bushes[i - 1] + bushes[i] + bushes[i + 1] > max:
        max = bushes[i - 1] + bushes[i] + bushes[i + 1]
print(f'Максимальное количество ягод равно: {max}')