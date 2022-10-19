def new_file ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as f:
        f.write(f'Фамилия; Имя; Номер телефона; Описание\n')