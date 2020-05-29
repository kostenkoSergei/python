try:
    class Worker:
        def __init__(self, name, surname, pos, wage, bonus):
            self.name = name
            self.surname = surname
            self.position = pos
            if not (isinstance(wage, int) or isinstance(bonus, float) or
                    isinstance(wage, int) or isinstance(bonus, float)):
                print('Оклад и премия должны быть числами!')
            self._income = {'wage': wage, 'bonus': bonus}


    class Position(Worker):
        def get_full_name(self):
            return print(f'{self.name} {self.surname}, {self.position}')

        def get_total_income(self):
            return print('Доход с учетом премии:', self._income['wage'] + self._income['bonus'])


    worker1 = Position(name='Иван', surname='Иванов', pos='инженер', wage=50000, bonus=3000)
    worker1.get_full_name()
    worker1.get_total_income()
    worker2 = Position(name='Петр', surname='Петров', pos='менеджер', wage=65000, bonus=4000)
    worker2.get_full_name()
    worker2.get_total_income()
    print(worker1.__dict__, worker2.__dict__, sep='\n')
except AttributeError as a:
    print(f'Вы ввели нечисловые значения оклада и премии, ошибка: {a}')
except TypeError as t:
    print(f'Вы ввели нечисловые значения оклада и премии, ошибка: {t}')
