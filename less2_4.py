# работа со строкой: вывод слов нумерованным списком
user_list = list(input('Введите несколько слов через пробелы: ').split(' '))
for i, el in enumerate(user_list, 1):
    print(i, el[:10])
