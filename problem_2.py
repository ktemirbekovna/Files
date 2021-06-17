'''Создайте файл users.txt. Напишите программу которая спрашивает у 
пользователя его Логин и Пароль и записывает в файл users.txt.'''

a = open("users.txt", "a")
b = input("login: ")
c = input("password: ")
a.write(b)
a.write(",\n")
a.write(c)
a.close()


