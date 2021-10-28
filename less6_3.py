class Worker:

    def __init__(self, name, sername, position, wage, bonus):
        self.name = name
        self.sername = sername
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, sername, position, wage, bonus):
        super().__init__(name, sername, position, wage, bonus)
        self.wage = wage
        self.bonus = bonus

    def get_full_name(self):
        return f'{self.name} {self.sername}'

    def get_total_income(self):
        return self.wage + self.bonus


person_1 = Position('Иван', 'Иванов', 'директор', 100000, 50000)
print(person_1.get_full_name())
print(person_1.get_total_income())
