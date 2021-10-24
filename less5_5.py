# Создаем список чисел
from random import randint

num_str = ""
for i in range(0, 5):
    num_str += str(randint(0, 101)) + " "
print(num_str)

# Записываем числа в файл
with open("task_5-5.txt", "w+") as num_file:
    num_file.write(num_str[:-1])

# суммируем числа из файла
with open("task_5-5.txt", "r+") as num_file:
    sum_list = num_file.read().split(' ')
    summing = 0
    for el in sum_list:
        summing += int(el)
print(f"Сумма чисел в файле равна {summing}")
