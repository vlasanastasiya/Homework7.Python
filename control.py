from os.path import exists
from create import new_file


def add_op():
    print("Необходимо заподнить данные: ")
    flag = True
    while flag:
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        number = input("Введите номер телефона: ")
        description = input("Введите описание: ")
        save = input("\n Нажмите 1 для сохранения либо любую другую цифру для выхода")
        if save == "1":
            write_op(surname, name, number, description)
        else:
            flag = False



def write_op(surn, na, num, descr):
    with open(file, "a", encoding = 'utf-8') as data:
        data.write(f"{surn}, {na}, {num}, {descr};\n") 

def read_op():
    file = 'Phonebook.csv'
    with open (file, 'r', encoding = 'utf-8') as data:
        print(data.read())

file = 'Phonebook.csv'
valid = exists(file)
if not valid:
    new_file()

