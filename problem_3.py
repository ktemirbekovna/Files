'''Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, 
то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. 
Подсказка: используйте ключевое слово in.'''

t = open("tekst_3.txt", "w")
t.write("s kj sw, v jsvjsklpqpdmlakcnl,x,';,JHBA KkZKMWPFMMSMC")
t.close()
v = open("tekst_3.txt", "r")
if 'w' in v.read():
	print("Да,в тексте есть w ")
else:
    print("Нет,в тесте нет w ")	