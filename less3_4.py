"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def decline(real_positive, negative_integer):
    """
    Raising the number x to the power of y (x > 0,  y <= 0)

    :param real_positive: float
    :param negative_integer: int, <= 0
    :return: float, positive
    """
    return real_positive ** negative_integer


def my_decline(real_positive, negative_integer):
    """
    Raising the number x to the power of y (x> 0, y<=0) using a loop

    :param real_positive: float
    :param negative_integer: int, <= 0
    :return: float, positive
    """
    result = float(1)
    while negative_integer < 0:
        result = result / real_positive
        negative_integer += 1
    return result


user_x = float(input('Введите действительное положительное число: '))
user_y = int(input('Введите целое отрицательное число: '))
print(f'Число {user_x} в степени {user_y} равно {decline(user_x, user_y)}')
print(f'Число {user_x} в степени {user_y} равно {my_decline(user_x, user_y)}')
