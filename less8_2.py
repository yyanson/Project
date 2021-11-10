class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое: ')
b = input('Введите делитель: ')
try:
    if float(b) == 0:
        raise OwnError('Делить на ноль нельзя!')
    c = float(a) / float(b)
    print('%.2f' % c)
except OwnError as err:
    print(err)
except ValueError:
    print('Вы ввели не число!')
