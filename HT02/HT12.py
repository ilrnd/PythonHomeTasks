# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input('Введите сумму чисел: '))
product = int(input('Введите произведение чисел: '))
flag = False
for i in range(1, sum, 1):
    for j in range(1, product, 1):
        if i + j == sum and i * j == product:
            print(i, j)
            flag = True
    if flag: break
if not flag:
    print('Введены некорректные сумма и произведение')