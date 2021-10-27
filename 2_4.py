# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_string = input('введите строку ').split()
# test_string = 'hellow   word aaaafafafafffaff@@@@ 1234567890123456789'.split()
# print(test_string.split())
for i, word in enumerate(my_string):
    print(i, word[:10])
