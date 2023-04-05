import os
os.system('clear')
file_path = "file.txt"


def append_list(stroka: str):
    list_1 = list()
    with open(file_path, 'a', encoding='UTF-8') as fa:
        list_1.append(stroka)
        fa.write(str(*list_1))
    return(list_1)

def search(stroka: str) -> str:
    with open(file_path, "r", encoding="UTF-8") as fr:
        list_search = list()
        for line in fr:
            for word in line.split():
                if stroka in word.casefold():
                    list_search.append(line)
                    break
        return list_search


def output():
    id = 0
    with open(file_path, "r", encoding="UTF-8") as fr:
        for line in fr:
            id += 1
            print(f'{id}. {line}', end='')


def search_delete(stroka: str): 
    with open(file_path, "r", encoding="UTF-8") as fr:
        list_out = [line.rstrip() for line in fr if line not in search(stroka)]
        
    with open(file_path, 'w', encoding='UTF-8') as fw:
        for line in list_out:
            fw.writelines(line +'\n')


while True:
    command = input("\nВведите команду (a - добавление данных, o - открытие данных, s - поиск данных\n d - удаление данных, c - изменение данных, q - выход): ")
    if command == 'q':
        break
    if command == 'a':
        append_list(input('Введите фамилию: ') + ' ')
        append_list(input('Введите имя: ') + ' ')
        append_list(input('Введите отчество: ') + ' ')
        append_list(input('Введите телефон: '))
        append_list('\n')
    if command == 'o':
        output()
    if command == 's':
        print(*search(input('Введите поисковой запрос: ').casefold()))
    if command == 'd':
        output()
        search_delete(input('Введите запрос для удаления: ').casefold())
        output()
    if command == 'c':
        output()
        search_delete(input('Введите запрос для изменения: ').casefold())
        append_list(input('Введите фамилию: ') + ' ')
        append_list(input('Введите имя: ') + ' ')
        append_list(input('Введите отчество: ') + ' ')
        append_list(input('Введите телефон: '))
        append_list('\n')
        output()


