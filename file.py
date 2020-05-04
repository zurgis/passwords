from os.path import isfile
import json
import os

def password_dir():
    """Создаем директорию для хранения файлов с паролями"""
    name_dir = 'password' # Наименование папки, где хранятся пароли
    try:
        os.mkdir(name_dir)
    except OSError:
        pass   
    os.chdir(name_dir)


def read_file(file_name):
    """Получаем значения из файла, если он существует"""
    template = {}
    if isfile(file_name): # Проверяем на наличие файла
        with open(file_name) as p:
            try: # Проверяем, что в файле есть данные для чтения
                info = json.load(p)
            except json.JSONDecodeError:
                pass
            else:
                for k, v in info.items():
                    num_pass = int(k)
                    template[num_pass] = v # Заносим в словарь данные о текущих паролях
                num_pass += 1 # Увеличиваем номер пароля на 1, для последующих действий
    else:
        num_pass = 1 # Устанавливаем значение по умолчанию, если нет файла
    return template, num_pass


def get_next_file(file_index, file_name):
    """Получаем следующий файл"""
    #template.clear() # Очищаем полученные данные, чтобы записать из нового файла
    file_index += 1
    file_name = 'password' + str(file_index) + '.json'
    return file_index, file_name