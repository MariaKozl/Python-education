class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} - машина поехала')

    def stop(self):
        print(f'{self.name} - машина останвилась')

    def turn(self, direction):
        print(f"Машина {self.name} повернула 'налево' if direction == 0 else 'направо'")

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed}')

class TownCar(Car):

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed} - превышение скорости!!!'\
            if self.speed > 60 else f'Скорость автомобиля {self.name} - {self.speed}'

class SportCar(Car):
    """спортивный автомобиль"""

class WorkCar(Car):

    def show_speed(self):
        return f'Скорость автомобиля {self.name}- {self.speed} - превышение скорости!!!'\
            if self.speed > 40 else f'Скорость автомобиля {self.name} - {self.speed}'

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

# sport_car = SportCar('Ferrari', 'red', 350)
# sport_car = SportCar.stop
police_car = PoliceCar('ДПС', 'белый', 110)
police_car.go()
