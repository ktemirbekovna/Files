if input('Хотите войти или зарегистрироваться? Y/n').lower() in 'y':
    file = open('/home/karlygach/class/files/database.txt', 'r')
    log = input('Login: ')
    f = file.read().split()
    if log in f:
        print('Имя пользователя сущствует.')
        input('Введите пароль: ')
        print('Вы успешно вошли в систему.')
    else:
        print('Имя пользователя отсутствует. Зарегистрируйтесь.')
    
    with open('/home/karlygach/class/files/database.txt', 'r') as f:
        t = f.read()
        enLog = input('Login: ')
        enPass = input('Password: ')
        enPass2 = input('Password: ')
    if enPass2 == enPass in t:
        print('Поздравляю! Вы успешно зарегистрированы!')
    else:
        print('Введенные пароли не совпадают.')