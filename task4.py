try:
    class Car:
        def __init__(self, speed: int = 0, color: str = 'unknown', name: str = 'unknown', is_police: bool = False):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police
            self.go()

        def go(self):
            print('Машина поехала')

        def stop(self):
            print('Машина остановилась')

        def turn(self, direction):
            print(f'Машина повернула {direction}')

        def show_speed(self):
            print(f'Текущая скорость автомобиля: {self.speed} км/ч')


    class TownCar(Car):
        def __init__(self, **kwargs):
            print('Машина для езды по городу')
            super().__init__(**kwargs)

        def get_car_info(self):
            if not self.is_police:
                print(f'Марка авто: {self.name}, цвет: {self.color}')
            else:
                print(f'Марка авто: {self.name}, цвет: {self.color}, машина является полицейской')

        def show_speed(self):
            if self.speed < 60:
                print(f'Текущая скорость автомобиля: {self.speed} км/ч')
            else:
                print(f'Текущая скорость автомобиля: {self.speed} км/ч. Скорость превышена на {self.speed - 60} км/ч')


    class SportCar(Car):
        def __init__(self, bodywork='неопределенный', **kwargs):
            print('Спортивный автомобиль')
            self.bodywork = bodywork
            super().__init__(**kwargs)

        def get_car_info(self):
            if not self.is_police:
                print(f'Марка авто: {self.name}, цвет: {self.color}')
            else:
                print(f'Марка авто: {self.name}, цвет: {self.color}, машина является полицейской')


    class WorkCar(Car):
        def __init__(self, **kwargs):
            print('Сервисный/рабочий автомобиль')
            super().__init__(**kwargs)

        def get_car_info(self):
            if not self.is_police:
                print(f'Марка авто: {self.name}, цвет: {self.color}')
            else:
                print(f'Марка авто: {self.name}, цвет: {self.color}, машина является полицейской')

        def show_speed(self):
            if self.speed < 40:
                print(f'Текущая скорость автомобиля: {self.speed} км/ч')
            else:
                print(f'Текущая скорость автомобиля: {self.speed} км/ч. Скорость превышена на {self.speed - 40} км/ч')


    class PoliceCar(Car):
        def __init__(self, **kwargs):
            print('Полицейский автомобиль')
            super().__init__(**kwargs)

        def get_car_info(self):
            if not self.is_police:
                print(f'Марка авто: {self.name}, цвет: {self.color}')
            else:
                print(f'Марка авто: {self.name}, цвет: {self.color}, машина является полицейской')


    town_car1 = TownCar(speed=45, name='Audi', color='red')
    town_car1.get_car_info()
    town_car1.turn('непонятно куда')
    town_car1.show_speed()
    town_car1.stop()
    print(town_car1.__dict__)
    print()
    town_car2 = TownCar(speed=200, name='BMW', color='yellow')
    town_car2.get_car_info()
    town_car2.show_speed()
    print(town_car2.__dict__)
    print()
    police_car = PoliceCar(speed=200, name='УАЗ', color='black', is_police=True)
    police_car.get_car_info()
    police_car.turn('ловить преступников')
    police_car.show_speed()
    print(police_car.__dict__)
    print()
    work_car1 = WorkCar(speed=100, name='Газель', color='blue')
    work_car1.get_car_info()
    work_car1.show_speed()
    print(work_car1.__dict__)
    print()
    sport_car1 = SportCar(speed=180, name='Запорожец', color='серо-буро-малиновый', bodywork='купе')
    sport_car1.get_car_info()
    sport_car1.turn('дрифтить')
    sport_car1.show_speed()
    print(sport_car1.__dict__)
except TypeError as t:
    print('Скорость должна быть числом', t)
