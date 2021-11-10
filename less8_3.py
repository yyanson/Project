class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
a = ''
while a != 'stop':
    user_a = input('Введите число (цифрами), если завершить -  слово "stop" : ')
    a = user_a
    try:
        if user_a.isalpha():
            raise OwnError('Ошибка ввода')
        num_list.append(float(user_a))
    except OwnError as err:
        print(err)
    except Exception:
        print('Вы ввели не число!')
print(num_list)
