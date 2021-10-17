"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(var_1, var_2, var_3):
    """

Summation of two maximum arguments

    :param var_1: float
    :param var_2: float
    :param var_3: float
    :return: float
    """
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)


nums = list((input('Введите три числа через пробел: ')).split(' '))
print(my_func(float(nums[0]), float(nums[1]), float(nums[2])))
