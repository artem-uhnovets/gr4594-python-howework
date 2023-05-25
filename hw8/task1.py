"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Дополнить телефонный справочник возможностью изменения и удаления данных.

Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных

"""
import os
import shutil

os.chdir('C:/Users/uhnov/OneDrive/Рабочий стол/УЧЕБА GB/PYTHON/HomeWorks/hw8')
print(os.getcwd())

clear = lambda: os.system('cls')
clear()

def input_number(text) -> int:
    print(text, end='')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('Пожалуйста введите число - ', end='')
            continue
        else:
            break
    return number

def horiz_line(text):
    print(('=' * ((len(text)*2)-1)) if type(text) == str else ('=' * max(list(map(lambda a: len(a),text)))))
    print(*text)
    print(('=' * ((len(text)*2)-1)) if type(text) == str else ('=' * max(list(map(lambda a: len(a),text)))))

def delete_modif_func(users_del_list, modify=None):
    if users_del_list:
        horiz_line(list(map(lambda num, usr: f'\n{num}. {usr[:-1]}\n', range(1, len(users_del_list) + 1), users_del_list)))
        while True:
            match key_choose_user := input('\nВЫХОД - чтобы завершить \nВыберите контакт - ').lower():
                case num if num.isdigit() and (int(num) in range(1,len(users_del_list) + 1)):
                    user_for_del = users_del_list[int(key_choose_user) - 1]
                    with open('task1.txt', 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    with open('task1.txt', 'w', encoding='utf-8') as f:
                        for line in lines:
                            if user_for_del not in line:
                                f.write(line)
                            elif modify == 'm': 
                                while True:
                                    modify_choose_list = ['1. фамилия', '2. имя', '3. отчество', '4. телефон', '5. полностью']
                                    print(*list(map(lambda a: f'\n{a}', modify_choose_list)))
                                    match modify_choose := input_number('\nКакие данные редактируем? '):
                                        case num if num in range(1,5):
                                            modify_line_list = line.split()
                                            modify_line_list[modify_choose - 1] = input('Введите новые данные - ')
                                            new_data = ' '.join(modify_line_list)
                                            f.write(f'{new_data}\n')
                                            break
                                        case 5:
                                            new_data = input('Отредактируйте новые данные полностью - ')
                                            f.write(f'{new_data}\n')
                                            break
                                        case _:
                                            horiz_line('Ошибка ввода! Введите от 1 до 5!') 
                    break
                case 'выход' | 'quit' | 'exit' | 'ds[jl':
                    break
                case _:
                    horiz_line('Ошибка ввода!')
    else:
        horiz_line('Никто не найден!')

def single_or_multy_search(text, num=None):
    if num == None:    
        with open('task1.txt', 'r', encoding='utf-8') as f:
            file = f.readlines()
            search = input(text).lower()
            if len(search.split()) > 1:
                search_list = set()
                for line in set(search.split()):
                    search_list = search_list.union(set(filter(lambda usr: line in usr.lower(), file)))
                return list(search_list)
            else:
                return list(filter(lambda usr: search in usr.lower(), file))
    else:
        with open('task1.txt', 'r', encoding='utf-8') as f:
            file = f.readlines()
            search = input(text).lower()
            if len(search.split()) > 1:
                search_list = set()
                for line in set(search.split()):
                    search_list = search_list.union(set(filter(lambda usr: line in (usr.lower().split())[num], file)))
                return list(search_list)
            else:
                return list(filter(lambda usr: search in (usr.lower().split())[num], file))

def delete_modify_user(modify = None):
    menu_search('Характеристика поиска:')
    search_choose_list = ['фамилию', 'имя', 'отчество', 'телефон']
    while True:
        match action := input('\nВыберите опцию поиска - '):
            case num if action.isdigit() and int(num) in range(1,5):
                delete_modif_func(single_or_multy_search(f'Введите {search_choose_list[int(num) - 1]} - ', (int(num) - 1)), modify)
                menu_search('Характеристика поиска:')
            case '5':
                delete_modif_func(single_or_multy_search('Введите ключевое(ые) слово(а) - '), modify)                                                                                                                                       
                menu_search('Характеристика поиска:')
            case '6' | 'выход' | 'quit' | 'exit' | 'menu' | 'main' | 'main menu' | 'menu main' | 'ds[jl':
                break
            case _:
                horiz_line('Нет такой функции!')
                menu_search('Характеристика поиска:')
         
def search_user():
    menu_search('Характеристика для поиска:')
    search_choose_list = ['фамилию', 'имя', 'отчество', 'телефон']
    while True:
        match action := input('\nВыберите опцию поиска - '):
            case num if action.isdigit() and int(num) in range(1,5):
                search_list = single_or_multy_search(f'Введите {search_choose_list[int(num) - 1]} - ', (int(num) - 1))
                if search_list:
                    horiz_line(list(map(lambda num, usr: f'\n{num}. {usr[:-1]}\n', range(1, len(search_list) + 1), search_list)))
                else:
                    horiz_line('Никто не найден!')
                menu_search()
            case '5':
                search_list = single_or_multy_search('Введите ключевое(ые) слово(а) - ')                                                                                                                                        
                if search_list:
                    horiz_line(list(map(lambda num, usr: f'\n{num}. {usr[:-1]}\n', range(1, len(search_list) + 1), search_list)))
                else:
                    horiz_line('Никто не найден!')
                menu_search()
            case '6' | 'выход' | 'quit' | 'exit' | 'menu' | 'main' | 'main menu' | 'menu main':
                break
            case _:
                horiz_line('Нет такой функции!')
                menu_search()

def add_user():
    with open('task1.txt', 'a', encoding='utf-8') as f:
        new_data = input('Введите по формату Фамилия Имя Отчество Телефон - ')
        f.write(f'{new_data}\n')

def read_all_users():
    with open('task1.txt', 'r', encoding='utf-8') as f:
        users_all_list = list(map(lambda a: a[:-1], f.readlines()))
        horiz_line(list(map(lambda num, usr: f'\n{num}. {usr}\n', range(1,len(users_all_list) + 1), users_all_list)))

def menu_search(text):
    menu_search_list = [text,
                        '1. По фамилии',
                        '2. По имени',
                        '3. По отчеству',
                        '4. По телефону',
                        '5. Любое совпадение',
                        '6. В главное меню']
    print(*map(lambda a: f'\n{a} ', menu_search_list))

def menu_main_info():
    menu_main_list = ['1. Показать все контакты',
                      '2. Добавить контакт',
                      '3. Поиск контакта',
                      '4. Удалить контакт',
                      '5. Редактировать контакт',
                      '6. Выход']
    print(*map(lambda a: f'\n{a} ', menu_main_list))

def menu_main():
    menu_main_info()
    while True:
        match user_action := input("\nВыберите функцию, через цифру - ").lower():
            case '1' | 'показать' | 'show':
                read_all_users()
                menu_main_info()
            case '2' | 'добавить' | 'add':
                add_user()
                menu_main_info()
            case '3' | 'поиск' | 'search':
                search_user()
                menu_main_info()
            case '4' | 'удалить' | 'del' | 'delete':
                delete_modify_user()
                menu_main_info()
            case '5' | 'редактировать' | 'modify' | 'edit':
                delete_modify_user('m')
                menu_main_info()
            case '6' | 'выход' | 'quit' | 'exit' | 'ds[jl':
                break
            case _:
                horiz_line("!!!Нет такой функции!!!")
                menu_main_info()

menu_main()