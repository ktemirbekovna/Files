'''Создайте текстовый файл python.txt и запишите в него текст #1 из Classroom:

Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит

букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,

выведите на экран все полученные слова. Подсказка: используйте for.'''


a = open('/home/karlygach/class/files/python.txt', 'r')
t_words = [ ]
v = (a.read().split())
for b in v:
    if "t" in b:
        t_words.append(b)
    if "T" in b:
        t_words.append(b)
print(t_words)
a.close()