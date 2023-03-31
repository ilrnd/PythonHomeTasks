# Задача 34
# пара-ра-рам рам-пам-папам па-ра-па-дам
import os
os.system('clear')
def winnie(song, alphabet):
    set_ = set()
    for word in song:
        count = 0
        for letter in word:
            if letter in alphabet:
                count += 1
        set_.add(count)
    return len(set_) 

set_alphabet = {'а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я'}

song = input().lower().split()
if winnie(song, set_alphabet) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')