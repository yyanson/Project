from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.v = size

    @property
    def material(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.h = height

    @property
    def material(self):
        return self.h * 2 + 0.3


c_1 = Coat(52)
s_1 = Suit(1.80)
total = c_1.material + s_1.material
print(c_1.material, s_1.material, total)

print(f'Coat (50 size): {Coat(50).material:.2f}\nSuit (190 height): {Suit(1.90).material:.2f}\n'
      f'Total material: {Coat(50).material + Suit(1.90).material:.2f}')
