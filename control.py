import json

from file import read_file, get_next_file
from utils import generate_password

# CONSTANTS
max_pass = 2 # Максимальное кол-во паролей в одном файле
password = generate_password()

def find_app(template, name_app):
    """Ищет приложение в шаблоне"""
    for value in template.values():
        if name_app in value:
            return value[name_app]
    return None


def find_login(items, login):
    """Ищет совпадение логина в приложении"""
    for item in items:
        if login == item['login']:
            return True
    return False


def search(file_name, file_index, name_app):
    """Осуществляет поиск по файлам"""
    while True:
        template, num_pass = read_file(file_name)
        items = find_app(template, name_app)
        if items:
            print(f'Приложение: {name_app}'.upper())
            for item in items:
                print(f'Логин: {item["login"]} \t Пароль: {item["password"]}')
            break

        if num_pass > max_pass: # Проверка на кол-во паролей в файле, если True, получаем след. файл
            file_index, file_name = get_next_file(file_index, file_name)
        else:
            break

    if not items:
        print('Такого приложения не существует')


def create(file_name, file_index, name_app):
    """Создаем новую запись"""
    login = input('Введите логин: ')
    save = True # Устанавливаем флаг на сохранение, если приложение создается первый раз

    while True:
        template, num_pass = read_file(file_name)
        items = find_app(template, name_app)
        if items:
            found = find_login(items, login)
            if found: # Если приложение и логин есть в файле
                print('Такая запись уже существует')
                save = False
                break
            else: # Если найдено только приложение, то добавляем в него новую пару логин-пароль
                items.append({'login': login, 'password': password})
                print(f'Пароль создан: {password}')
                save = False
                break
        else:
            if num_pass > max_pass:
                file_index, file_name = get_next_file(file_index, file_name)
            else:
                break
    if save:
        template[num_pass] = {name_app: [{'login': login, 'password': password}]}
        print(f'Пароль создан: {password}')
    
    with open(file_name, 'w') as p:
        json.dump(template, p, indent=4, sort_keys=True)


def change(file_name, file_index, name_app):
    """Изменяет пароль"""
    save = True

    while True:
        template, num_pass = read_file(file_name)
        items = find_app(template, name_app)
        if items:
            login = input('Введите логин: ')
            found = find_login(items, login)
            if found:
                for item in items:
                    if login == item['login']:
                        item['password'] = password # Заменяем старый пароль, на новый сгенерированный
                        print(f'Новый пароль создан: {password}')
                break
            else:
                print('Такого логина не существует')
                save = False
                break
        else:
            if num_pass > max_pass:
                file_index, file_name = get_next_file(file_index, file_name)
            else:
                print('Такого приложения не существует')
                save = False
                break
    
    if save:
        with open(file_name, 'w') as p:
            json.dump(template, p, indent=4, sort_keys=True)