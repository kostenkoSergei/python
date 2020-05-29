class Stationery:
    def __init__(self, x):
        self.title = x

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} Запуск отрисовки маркером')


pen1 = Pen('ручка')
pen1.draw()
pencil1 = Pencil('карандаш')
pencil1.draw()
handle1 = Handle('маркер')
handle1.draw()
