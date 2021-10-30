'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
 Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def my_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return " enter float"
    return res


print(my_fun(22.3, -5))
