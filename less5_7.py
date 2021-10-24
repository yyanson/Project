import json
dict_firm = {}
with open('task_5-7.txt', 'r') as data_file:  # открываем файл с данными
    n, summing = 0, 0  # промежуточные переменные
    for line in data_file:
        line_list = line.split(' ')  # преобразуем строку в список элементов
        profit = int(line_list[2]) - int(line_list[3])  # вычисляем прибыль по каждой фирме
        if profit > 0:  # если фирма с прибылью
            n += 1  # считаем количестыо фирма с прибылью
            summing += profit  # суммируем все прибыли
        dict_firm.update({line_list[0]: profit})  # добавляем данные в словарь фирм
avr_dict = {"average_profit": '%.2f' % (summing / n)}  # создаем словарь о средней прибыли
my_json = ([dict_firm, avr_dict])  # создаем список для json-объекта
print(my_json)  # проверка

with open('task_5-7_json.txt', 'w+') as file_json:  # создаем файл для json-объекта
    json.dump(my_json, file_json)  # записываем в файл json-объект
