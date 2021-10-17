"""Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно
добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_list_nums(any_list):
    """
Summing float and int items in a list

    :param any_list: list
    :return: float
    """
    sum_el = float(0)
    for el in any_list:
        try:
            el = float(el)
        except ValueError:
            el = float(0)
        sum_el += el
    return sum_el


stop = 0
all_sum = float(0)
while stop != 1:
    user_list = list((input('Введите числа через пробел (если хотите завершить, введите в конце символ "s"): ')).split(
        " "))
    if set(user_list).intersection('s'):
        stop = 1
        user_list.remove('s')
    all_sum += sum_list_nums(user_list)
    print(f'Сумма введеных чисел равна: {all_sum}')
