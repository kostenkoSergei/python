class Road:
    def __init__(self, x, y):
        """Конструктор базового класса"""
        self._length = x
        self._width = y

    def calc(self, x, y):
        """Возвращает занчение массы асфальта  для покрытия полотна с заданными толщиной и массой асфльта"""
        return self._length * self._width * x * y


try:
    some_road = Road(float(input('Длина дорожного полотна,м.: ')), float(input('Ширина дорожного полотна, м.: ')))
    mass = some_road.calc(float(input('Масса асфальта для покрытия 1 см., кг.: ')),
                          float(input('Толщина полотна, см.: ')))
    print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {round((mass / 1000), 2)} т.')
except ValueError as v:
    print('Вводимые параметры должны быть числами!', v, sep='\n')
