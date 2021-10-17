""" Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""


def personal_data(f_name, l_name, year, city, email, telephone, space=' '):
    """
    Summing string arguments into a single line with a space between the arguments

    :param f_name: string
    :param l_name: string
    :param year: string dd.mm.yy
    :param city: string
    :param email: string
    :param telephone: string
    :param space: string
    :return: string

    """
    return f_name + space + l_name + space + year + space + city + space + email + space + telephone


user_f_name = input('Введите имя: ')
user_l_name = input('Введите фамилию: ')
user_year = input('Введите год рождения: ')
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_telephone = input('Введите номер телефона: ')
print(personal_data(user_f_name, user_l_name, user_year, user_city, user_email, user_telephone))

# пользовательский разделитель:
print(personal_data(user_f_name, user_l_name, user_year, user_city, user_email, user_telephone, '/'))
