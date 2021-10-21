from functools import reduce


def multi(el_1, el_2):
    return el_1 * el_2


my_list = [i for i in range(100, 1001, 2)]
print(reduce(multi, my_list))
