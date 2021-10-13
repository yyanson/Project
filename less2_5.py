# Рейтинг
my_list = [7, 5, 3, 3, 2]
game = 1
while game != 0:
    user_num = int(input('Ведите число: '))
    new_list = my_list.copy()
    new_list.append(user_num)
    new_list.sort(reverse=True)
    print('Рейтинг:', new_list)
    game = int(input('Продолжаем? Нет - 0, да - 1: '))
