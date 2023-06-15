# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from os import path
from sys import argv



all_data = []
last_id = 0
file_base = "base.txt"

if not path.exists(file_base):
    with open(file_base, 'w', encoding='utf-8') as f:
        pass


def exit():
    print('yes or no?')
    ex = input()
    if ex == 'yes':
        print('exit')
        quit()

def read_records():
    global all_data, last_id

    with open(file_base, encoding='utf-8') as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []





def show_all():
    if all_data:
        print(*all_data, sep='\n')
    else:
        print('Empty data')

def add_new_rescord():
    global last_id

    array = ['Surname:', 'Name:', 'Patronymic:', 'Phone number:']
    string = ''

    for i in array:
        string += input(f'Enter {i} ') + ' '
    last_id += 1

    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(f'{last_id} {string}\n')

def main_menu():
    play = True
    while play:
        read_records()
        answer = input('Phone book:\n'
                       '1.Show all records\n'
                       '2.Add a record\n'
                       '3.Search a record\n'
                       '4.Change\n'
                       '5.Delete\n'
                       '6.Imp\Exp\n'
                       '7.Exit\n')
        match answer:
            case '1':
                show_all()
            case '2':
                add_new_rescord()
            case '3':
                pass
            case '4':
                pass
            case '5':
                play = False
            case '6':
                pass
            case '7':
                exit()
            case _:
                print("Try again!\n")


main_menu()