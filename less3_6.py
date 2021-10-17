"""Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
"""


def int_func(lat_word):
    """

Uppercase fo the first item in string

    :param lat_word: string
    :return: string
    """
    return lat_word[0].upper() + lat_word[1:]


user_word = input('Введите слово из латинских букв: ')
print(int_func(user_word))
