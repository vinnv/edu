#1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
bolean=True
print(type(bolean),bolean)

float=0.1111
print(type(float),float)

number_one = input('введите первое число:')
print(type(number_one), number_one)

number_twoo = input('введите второе число:')
print(type(number_twoo), number_twoo)

if number_one == number_twoo:
    print('числа одинаковые')
else:
    print('числа разные')

string = input('введите строку:')
print(type(string), string)

