# Проверка типа элементов в списке
my_list = [None, True, 1, 2.5, 2 + 3j, bin(17), 'text', ['a', 'b'], set([10, 34, 'abc', 10]),
           frozenset([10, 34, 'abc', 10]), (10, 2, 'abc', 10),
           {10: 'ten', 2: 'two', 'alphabet': 'abc'}]
for el in my_list:
    print(el, type(el))
