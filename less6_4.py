class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'the {self.name} went')

    def stop(self):
        self.speed = 0
        print(f'the {self.name} stopped')

    def turn(self, direction):
        print(f'the {self.name} turned to {direction}')

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed):
        self.speed = speed
        self.name = 'TownCar'
        self.color = 'green'
        self.is_police = False

    def show_speed(self):
        text = f'{self.name}: Warning, speeding!' if self.speed > 60 else f'{self.name} speed: {self.speed}'
        print(text)


class SportCar(Car):
    def __init__(self, speed):
        self.speed = speed
        self.name = 'SportCar'
        self.color = 'red'
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed):
        self.speed = speed
        self.name = 'WorkCar'
        self.color = 'yellow'
        self.is_police = False

    def show_speed(self):
        text = f'{self.name}: Warning, speeding!' if self.speed > 40 else f'{self.name} speed: {self.speed}'
        print(text)


class PoliceCar(Car):
    def __init__(self, speed):
        self.speed = speed
        self.name = 'PoliceCar'
        self.color = 'white'
        self.is_police = True


car_1 = TownCar(40)
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.speed = 70
car_1.show_speed()
car_1.stop()
car_1.show_speed()

car_2 = SportCar(140)
car_2.show_speed()

car_1 = WorkCar(40)
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.speed = 70
car_1.show_speed()
car_1.stop()
car_1.show_speed()

car_4 = PoliceCar(50)
print(car_4.name, car_4.speed, car_4.color, car_4.is_police)
