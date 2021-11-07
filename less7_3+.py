class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):  # вычитание для "нематематических" клеток
        if self.num != other.num:
            return Cell(abs(self.num - other.num))
        else:
            print('Клетки самоуничтожились!')  # Как сделать, чтобы это печталось в f-строке где надо, см. ниже в print?
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):  # деление для "нематематических" клеток
        return Cell(self.num // other.num if self.num > other.num else other.num // self.num)

    def make_order(self, val):
        draw_cell = ''
        for _ in range(self.num // val):
            draw_cell += '*' * val + '\n'
        draw_cell += '*' * (self.num % val) + '\n'
        return draw_cell


print('Сложение клеток:\n' + (Cell(17) + Cell(5)).make_order(5))
print('Вычитание клеток:\n' + (Cell(5) - Cell(16)).make_order(5))

# Как сделать, чтобы сначала печталось "Вычитание равных клеток:", а потом сообщение из метода "Клетки самоуничтожились"?
print('Вычитание равных клеток:\n' + (Cell(16) - Cell(16)).make_order(5))
print('Умножение клеток:\n' + (Cell(4) * Cell(5)).make_order(7))
print('Деление клеток:\n' + (Cell(31) / Cell(5)).make_order(5))
