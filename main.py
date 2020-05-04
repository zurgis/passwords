""" Приложение для генерации паролей, плюс запись в файл """

from string import ascii_letters, digits
from os.path import isfile
import random, json

from file import read_file, get_next_file, password_dir
from control import search, create, change

# GLOBAL VARIABLES
file_index = 0
file_name = 'password' + str(file_index) + '.json'

def main():
    while True:
        print('1) Найти')
        print('2) Создать')
        print('3) Изменить')
        print('4) Выйти')

        selection = int(input('Что хотите сделать? '))
        if selection == 1:
            name_app = input('Введите название приложения: ').lower()
            search(file_name, file_index, name_app)
            break
        elif selection == 2:
            name_app = input('Введите название приложения: ').lower()
            create(file_name, file_index, name_app)
            break
        elif selection == 3:
            name_app = input('Введите название приложения: ').lower()
            change(file_name, file_index, name_app)
            break
        elif selection == 4:
            break
        else:
            print('Неверное значение. Введите еще раз!')

if __name__ == "__main__":
    password_dir()
    main()