class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title} ')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self, color):
        print(f'Запуск отрисовки c помощью {color} {self.title}')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title}, а не Pen')


obj_1 = Pen()
obj_1.draw()

obj_2 = Pencil()
obj_2.draw('red')

obj_3 = Handle()
obj_3.draw()
