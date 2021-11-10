class Equipment:
    registry_list = {}

    def __init__(self, name, count):
        self.place = {}
        self.name = name
        self.count = Equipment.checking(count)  # проверка ввода числа пользователем при создании объекта
        self.place = {}

    @staticmethod
    def checking(user_num):
        if not (str(user_num).isdigit()):
            print('Неверный формат, для указания количества: введите натуральное число цифрами')
            return int(0)
        else:
            return int(user_num)

    def set_place(self, place, k):  # смена места нахождения техники
        if k > self.count:
            print(f'Перемещение {self.name} в количестве {k} шт. невозможно')
        elif self.place.get(place.name):
            p = k + self.place.get(place.name)
            self.place.update({place.name: p})
        else:
            self.place.update({place.name: k})

    @classmethod
    def registry(cls, tech, m):  # внесение техники в реест всей техники
        m = Equipment.checking(m)
        cls.registry_list.update({tech.name: m})


class Printer(Equipment):
    color = 'color'


class Scanner(Equipment):
    color = 'no'


class Xerox(Equipment):
    color = 'black'


class Division:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.tech = {}

    def getting(self, tech, c):  # подразделение получает технику
        if tech.name in self.tech.keys():
            self.tech.update({tech.name: c + self.tech.get(tech.name)})
        else:
            self.tech.update({tech.name: c})


class Warehouse(Division):
    def __init__(self, name, address):
        super(Warehouse, self).__init__(name, address)
        self.name = name
        self.giving = {}
        self.getting = {}
        self.listing = {}

    def adding(self, dict_l, tech, d):  # функция подсчета остатков после перемещения техники
        if dict_l.get(tech.name):
            d += dict_l.get(tech.name)
        else:
            d += 0
        return dict_l.update({tech.name: d})

    def get_tech(self, tech):  # получение техники на склад
        n = tech.count
        Equipment.registry(tech, n)
        self.getting.update({tech.name: n})
        if tech.name in self.listing.keys():
            self.adding(self.listing, tech, n)
        else:
            self.listing.update({tech.name: n})
        tech.set_place(self, n)

    def give_tech(self, tech, n, new_place):  # выдача техники со склада подразделению
        n = Equipment.checking(n)
        if tech.name in self.listing.keys():
            a = self.listing.get(tech.name)
        else:
            a = 0
        if a < n:
            print(
                f'Недостаточое количество: на складе {tech.name} {tech.count} шт., перемешение {n} шт. в {new_place.name} невозможно!')
        else:
            self.adding(self.listing, tech, -n)
            if tech.name in self.giving.keys():
                self.adding(self.giving.get(tech.name), new_place, n)
            else:
                self.giving.update({tech.name: {new_place.name: n}})
            tech.set_place(self, -n)
            tech.set_place(new_place, n)
            new_place.getting(tech, n)


class Office(Division):
    def __init__(self, name, address):
        super(Office, self).__init__(name, address)
        self.name = name
        self.address = address
        self.tech = {}


class Store(Division):
    def __init__(self, name, address):
        super(Store, self).__init__(name, address)
        self.name = name
        self.address = address
        self.tech = {}


sklad = Warehouse('sklad', '1-street, 12')
office = Office('office', '3-street, 10')
store = Store('store', '3-street, 10')

p_1 = Printer('Canon', 3)
p_2 = Printer('Laser', 4)
s_1 = Scanner('sk1', 2)
s_2 = Scanner('sk2', 1)
x_1 = Xerox('X1', 1)

sklad.get_tech(p_1)  # поступление на склад принтера
sklad.get_tech(p_2)  # поступление на склад принтера
sklad.get_tech(s_1)  # поступление на склад сканера
sklad.get_tech(s_2)  # поступление на склад сканера
sklad.get_tech(x_1)  # поступление на склад ксерокса
print(f'Equipment.registry_list: {Equipment.registry_list}')
print(f'sklad.listing: {sklad.listing}')
print(f'sklad.getting: {sklad.getting}')
print(
    f' {p_1.name}: {p_1.place}\n {p_2.name}: {p_2.place}\n {s_1.name}: {s_1.place}\n {s_2.name}: {s_2.place}\n {x_1.name}: {x_1.place}\n')

sklad.give_tech(p_1, 1, office)  # выдача со склад 1 принтера в офис
print(f'sklad.listing: {sklad.listing}')
print(f'sklad.giving: {sklad.giving}')
print(f'{p_1.name}: {p_1.place}')
print(f'office.tech: {office.tech}')

print('\n******')
sklad.give_tech(p_1, 2, office)   # выдача со склад еще 2 принтеров в офис
print(f'sklad.listing: {sklad.listing}')
print(f'sklad.giving: {sklad.giving}')
print(f'{p_1.name}: {p_1.place}')
print(f'office.tech: {office.tech}')

print('\n******')
sklad.give_tech(x_1, 1, store)   # выдача со склад единственного ксерокса
print(f'sklad.listing: {sklad.listing}')
print(f'sklad.giving: {sklad.giving}')
print(f'{x_1.name}: {x_1.place}')
print(f'store.tech: {store.tech}')

print('******')
sklad.give_tech(x_1, 1, office)    # попытка выдачи со склад ксерокса, которого уже нет
print(f'sklad.listing: {sklad.listing}')
print(f'sklad.giving: {sklad.giving}')
print(f'{x_1.name}: {x_1.place}')
print(f'office.tech: {office.tech}')
