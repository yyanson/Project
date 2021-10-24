"""
Файл 'task_5-3.txt':

Иванов 23543.12
Петров 13749.32
Сидоров 34289.23
Васин 13987.43
Федоров 45983.45
Алехин 23984.56
Денисов 67456.56
Никитин 34678.78
Юрьев 65298.56
Ильин 15983.67
Макаров 56456.12
"""
summ_salary, n, rich_list = 0, 0, []
print('Сотрудники с окладом меньше 20 тыс.: ')
with open('C:/PyProjects/first/task_5-3.txt', 'r') as salary:
    dict_salary = {}
    for line in salary:
        str_line = line.split(' ')
        if float(str_line[1].rstrip('/n')) < 20000.0:
            print(str_line[0])
        n += 1
        summ_salary += float(str_line[1].rstrip('/n'))
print(f'Средняя величина дохода сотрудников: {"%.2f" % (summ_salary/n)}')
