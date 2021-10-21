"""
Итератор, генерирующий целые числа, начиная с указанного;
Итератор, повторяющий элементы некоторого списка, определённого заранее.
"""
from itertools import count
from itertools import cycle

begin = int(input('Введите начальное число: '))
finish = int(input('Введите конечное число: '))
for el in count(begin):
    if el > finish:
        break
    else:
        print(el)

user_list = input('Введите список элеменов в виде строки: ')
user_end = int(input('Введите количество итераций: '))
i = 1
for elem in cycle(user_list):
    if i > user_end:
        break
    else:
        print(elem)
        i += 1
