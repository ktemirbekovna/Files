'''Создайте форму регистрации которая спрашивает у пользователя: Логин, Пароль и Фото. 
Заранее подготовьте фото на компьютере и когда программа спросит ваше фото просто укажите полный путь до места где лежит ваше фото. 
Программа должна проверить если фото правда существует по такому пути И также это фото с одним из 3 расширений("jpeg", "jpg", "png") 
то вы сохраняете в файл логин, 
пароль, путь до фото которое указал пользователь. 
А самому пользователю вы говорите о том что Регистрация Успешна!'''

if input('Хотите войти или зарегистрироваться? Y/n').lower() in 'y':
    Log = input('Login: ')
    Pass = input('Password: ')
    Photo = input('Your photo: ')
    a = open('/home/karlygach/class/files/avatar.jpg')
    if Photo in a:
        print('Вы зарегистрированы.')
    else:
        print('Файл отсутствует')