'''Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти или зарегистрироваться. 
Спросите его логин и пароль. Если такой логин уже есть скажите ему что логин уже существует и предложите авторизоваться с
просив пароль. Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.'''


if input('Хотите войти или зарегистрироваться? Y/n').lower() in 'y':
    file = open('/home/karlygach/class/files/database.txt', 'r')
    log = input('Login: ')
    f = file.read().split()
    while True:
        if log in f:
            print('Имя пользователя сущствует.')
            input('Введите пароль: ')
            print('Вы успешно вошли в систему.')
            break
        else:
            print('Имя пользователя отсутствует. Зарегистрируйтесь.')
        with open('/home/karlygach/class/files/database.txt', 'r') as f:
            t = f.read()
            enLog = input('Login: ')
            enPass = input('Password: ')
            enPass2 = input('Password: ')
        if enPass2 == enPass in t:
            print('Поздравляю! Вы успешно зарегистрированы!')
            break
        else:
            print('Введенные пароли не совпадают.')