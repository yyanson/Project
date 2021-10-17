"""В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""


def int_func(lat_word):
    """

Uppercase fo the first item in string

    :param lat_word: string
    :return title_word: string
    """
    try:
        title_word = lat_word[0].upper() + lat_word[1:]
    except IndexError:
        title_word = ''
    return title_word


def all_title(lower_string):
    """
Uppercase fo the first letters of all of the words in string

    :param lower_string: string
    :return title_string: string
    """

    word_list = lower_string.split(' ')
    title_string = ''
    for el in word_list:
        title_string = title_string + int_func(el) + ' '
    return title_string


user_string = input('Введите слова из латинских букв через пробелы: ')
print(all_title(user_string))
