""" Приложение для генерации паролей, плюс запись в файл """

from string import ascii_letters, digits
from os.path import isfile
import random, json

count_row = 100
min_length = 8
max_length = 10
file_index = 0
num_pass = 1

file_name = 'password' + str(file_index) + '.json'

# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890
text_to_generate = ascii_letters + digits

pass_length = random.randint(min_length, max_length)
pass_list = random.choices(text_to_generate, k=pass_length)

#for i in pass_list:
#    password += i
password = ''.join(pass_list)

name_app = input('Name app for password: ')
login = input('Enter login for password: ')

template = {}

while True:
    if isfile(file_name):
        with open(file_name) as p:
            try:
                info = json.load(p)
            except json.JSONDecodeError:
                pass
            else:
                for k, v in info.items():
                    num_pass = int(k)
                    template[num_pass] = v
                num_pass += 1

    if num_pass > 5:
        template.clear()
        file_index += 1
        num_pass = 1
        file_name = 'password' + str(file_index) + '.json'
    else:
        break               

def s_or_c(search_or_create, i):
    global flag

    if search_or_create == 'search':
        flag = True
        print(i['password'])
    elif search_or_create == 'create':
        accept = input('You want change to password? yes/no ')
        if accept == 'yes':
            i['password'] = password
            flag = True
        elif accept == 'no':
            flag = True
        else:
            print('Incorrect value. Password not change')
            flag = True

search_or_create = input('You want create or search password? create/search ')
flag = False
for value in template.values():
    for key, value in value.items():
        if key == name_app:
            for i in value:
                if i['login'] == login:
                    s_or_c(search_or_create, i)
            else:
                if not flag:
                    value.append({'login': login, 'password': password})
                    flag = True

if not flag:
    template[num_pass] = {name_app: [{'login': login, 'password': password}]}

with open(file_name, 'w') as p:
    json.dump(template, p, indent=4, sort_keys=True)

print('Password created:', password)