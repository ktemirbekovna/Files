while True:
    print('Войдите или зарегистрируйтесь')
    print('1.Регистрация.')
    print('0.Выход.')

q = input('Выберите действие: ')   
with open('Работа с файлами/home/karlygach/class/files/database.txt','r') as file:
	    users_db = {}
	    for i in file.readlines():
	    	logpass = i.split()
	    	value = []
	    	value.append(logpass[1])
	    	value.append(logpass[2])
	    	users_db[logpass[0]] = value
if q == "1":
	while True:
		username = input('Введите логин: ')
		if not(username in users_db.keys()):
			password = input('Введите пароль: ')
			photo_path = input('Введите путь к файлу; ')
			try:
				with open('Работа с файлами/' + photo_path, "rb"):
					with open('Работа с файлами/home/karlygach/class/files/database.txt','r') as file:
						file.write(username + ' ' + password + ' ' + photo_path + '\n')
					print('Вы успешно зарегистрировались\n')
					break
			except FileNotFoundError:
			    print('Файл не найден')
			else:
			    print('Пользователь с таким логином уже существует')    		
elif q == "0":
    break
else:
	print('Неправильный ввод\n')