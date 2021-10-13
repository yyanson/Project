# Обмен значений соседних элементов списка
user_list = list(input('Введите список элементов чрез пробелы: ').split(' '))
print(user_list)
k, i = len(user_list) // 2, 1
while i <= k:
    user_list[2 * i - 2], user_list[2 * i - 1] = user_list[2 * i - 1], user_list[2 * i - 2]
    i += 1
print(user_list)
