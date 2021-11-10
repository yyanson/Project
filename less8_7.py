class ComplexNum:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __str__(self):
        return f'{self.a} + {self.b} * j'

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


c = ComplexNum(1, 4)
d = ComplexNum(3.5, -6)
print(f' c: {c}\n d: {d}')
print(f' c + d: {c + d}')
print(f' c * d: {c * d}')
