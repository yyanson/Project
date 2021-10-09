# Результат работы фирмы
rev = float(input('Укажите финансовую выручку фирмы: '))
cst = float(input('Укажите издержки фирмы: '))
result = rev - cst
if result < 0:
    print(f'Фирма работает с убытком. Размер убытка: {result}')
else:
    rent = "%.1f" % (result * 100 / rev)
    print(f'Фирма работает с прибылью, размер прибыли: {result}')
    sht = int(input('Укажите численность сотрудников фирмы: '))
    staff_result = "%.2f" % (result / sht)
    print()
    print("{:<15} {:<15} {:<15}".format('Прибыль', 'Рентабельность', 'Прибыль на одного сотрудника'))
    print("{:<15} {:<15} {:<15}".format(result, rent + '%', staff_result))
