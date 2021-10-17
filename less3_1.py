# функция деления с исключением деления на ноль
def div_norm(var_1, var_2):
    """
Division, except division by zero

    :param var_1: float
    :param var_2: float
    :return: float
    """
    if var_2 == 0:
        print('Деление на ноль невоможно!')
        return
    else:
        return var_1 / var_2


user_var_1 = float(input('Введите делимое: '))
user_var_2 = float(input('Введите делитель: '))
print("Результат деления: ", div_norm(user_var_1, user_var_2))
