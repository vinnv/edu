'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''

name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')


def my_func(name, surname, year, city, email, telephone):
    return f"name - {name}; surname - {surname}; year - {year}; city - {city}; telephone - {telephone}"


# print(my_func(surname = 'ivanov', name = 'ivan', year = '1985', city = 'st. Petersburg', email = 'my@email.ru', telephone = '8-999-999-99-99'))
print((my_func(name, surname, year, city, email, telephone)))
