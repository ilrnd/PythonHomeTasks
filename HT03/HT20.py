# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
#  что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
import os
os.system('clear')
def find_in_dict(dic, text):
    for key in dic:
        if text in key:
            return dic[key]
    return False
    
dictionary_eng = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'): '1',
    ('D', 'G'): '2',
    ('B', 'C', 'M', 'P'): '3',
    ('F', 'H', 'V', 'W', 'Y'): '4',
    ('K'): '5',
    ('J', 'X'): '8',
    ('Q', 'Z'): '10',
    }

dic = {
    ('раз','два','три'): 'одна команда', 
    ('четыре','пять','шесть'): 'другая команда'
    }

dictionary_rus = {
    ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'): '1',
    ('Д', 'К', 'Л', 'М', 'П', 'У'): '2',
    ('Б', 'Г', 'Ё', 'Ь', 'Я'): '3',
    ('Й', 'Ы'): '4',
    ('Ж', 'З', 'Х', 'Ц', 'Ч'): '5',
    ('Ш', 'Э', 'Ю'): '8',
    ('Ф', 'Щ', 'Ъ'): '10'
    }
alphabet_eng = set()  # eng alphabet
for key in dictionary_eng:
    alphabet_eng |= set(key)
alphabet_rus = set()  # rus alphabet
for key in dictionary_rus:
    alphabet_rus |= set(key)
word = input('Введите слово: ')
sum = 0
word_upper = word.upper()
if word_upper[0] in alphabet_eng:
    for char in word_upper:
        sum += int(find_in_dict(dictionary_eng, char))
else:
    for char in word_upper:
        sum += int(find_in_dict(dictionary_rus, char)) 
print(f'Сумма ваших очков равна = {sum}')
