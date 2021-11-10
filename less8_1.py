class Data:
    def __init__(self, user_data):
        if user_data == '**-**-****':
            self.user_data = user_data
        else:
            print(f'Дата введена некорректно: {user_data}!')

    @classmethod
    def transform(cls, user_data):
        user_list = []
        for el in user_data.split('-'):
            user_list.append(int(el))
        return user_list

    @staticmethod
    def check(user_data):
        month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        data_list = Data.transform(user_data)
        c = 'Дата корректная'
        a = 'Неверно указан день! ' if data_list[0] < 1 or data_list[0] > (month_dict.get(data_list[1]) or 31) else ''
        a += 'Неверно указан месяц! ' if data_list[1] > 12 else ''
        a += 'Указанный год не високосный! ' if data_list[2] % 4 != 0 and data_list[:2] == [29, 2] else ''
        return a or c


my_data = Data('3333-22')
data = '332-14-3990'
print(Data.transform(data), Data.check(data))
print(Data.transform('332-10-1990'), Data.check('332-10-1990'))
print(Data.transform('32-14-1990'), Data.check('32-14-1990'))
print(Data.transform('32-12-1990'), Data.check('32-12-1990'))
print(Data.transform('31-12-1990'), Data.check('31-12-1990'))
print(Data.transform('00-12-1990'), Data.check('00-12-1990'))
print(Data.transform('30-02-1990'), Data.check('30-02-1990'))
print(Data.transform('29-02-2001'), Data.check('29-02-2001'))
