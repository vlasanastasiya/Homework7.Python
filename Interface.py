# def interface_menu ():
#     directory = []
#     surname = input('Введите фамилию: ')
#     directory.append(surname)
#     name = input('Введите имя: ')
#     directory.append(name)
#     phone_number = input('Введите номер телефона: ')
#     directory.append(phone_number)
#     description = input('Введите описание: ')
#     directory.append(description)
#     return directory

from control import add_op, read_op


def interface_menu():
    flag = True
    while flag:
        print('\nЗдравствуйте! Это телефонная книга! Выберите соответствующую цифру в меню: ')
        while True:
            print('1 - Добавить контакт')
            print('2 - Вывести все контакты')
            print('3 - Выйти из телефонной книги')
            choice = input()
            if choice not in ["1", "2", "3"]:
                print('Выберите другую цифру меню. ')
                continue
            elif choice == "1":
                add_op()
                break
            elif choice == "2":
                read_op()
            else:
                flag = False
                break