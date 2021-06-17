'''С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. 
Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir. 
В итоге у вас на рабочем столе должен появиться файл directories.txt. 
Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.'''


dip = open("/home/karlygach/Рабочий стол/directories1.txt", "a")
dip.write("class\n")
dip.write("HomeWork\n")
dip.write("snap\n")
dip.write("Документы\n")
dip.write("Музыка\n")
dip.write("Шаблоны\n")
dip.write("Desktop\n")
dip.write("my_box\n")
dip.write("Загрузки\n")
dip.write("Общедоступные\n")
dip.write("Изображения\n")
dip.write("Рабочий стол\n")
dip.close()