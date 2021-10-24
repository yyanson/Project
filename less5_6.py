import os
with open(os.getcwd() + r'\task_5-6.txt', 'r') as my_file:  # открываем файл для чтения - из текущей директории
    my_dict = {}  # создаем словарь
    for line in my_file:  # в каждой строке файла
        line_list = line.split(' ')  # преобразуем строку файла в список
        summing = 0
        for i in line_list:  # в каждом элементе строки берем только цифры
            i_new = ''  # создаем переменную для элемента из цифр - строкового формата
            for n in range(0, len(i)):  # проверяем каждый символ элемента
                i_new += i[n] if i[n].isdigit() else ''  # если символ цифра, добавляем его в строку из цифр
                i_new_int = int(i_new) if i_new.isdigit() else 0  # переводим "строку из цифр" в число
            summing += i_new_int  # суммируем числа в строке
        my_dict.update({line_list[0].replace(':', ''): summing})  # добаляем очищенные данные в словарь
print(f'my_dict  {my_dict}')


# дополнительно: запись данных в файл программным методом - гарантирована запись файла в текщую директорию
"""print(os.getcwd()) # находим рабочую директорию my_data_list = ['Информатика: 100(л) 50(пр) 20(лаб)', 'Физика: 30(
л) - 10(лаб)', 'Физкультура: - 30(пр) -', 'Химия: 25(л) - 15(лаб)'] print(len(my_data_list)) 

with open(os.getcwd() + r'\task_5-6.txt', 'w+') as my_file: # создаем файл
    for i in range(0, len(my_data_list)):
        my_file.writelines(my_data_list[i] + '\n') # записываем в файл данные

with open(os.getcwd() + r'\task_5-6.txt', 'r+') as my_file: # проверяем, что получилось
    for line in my_file:
        print(line)
"""