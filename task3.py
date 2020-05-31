class Cell:
    def __check(other):
        """To check if instance is instance of class Cell"""
        if isinstance(other, Cell):
            return True
        raise ValueError('You can perform actions only with class Cell instances!!!')

    def __init__(self, some_number):
        self.some_number = some_number

    def __str__(self):
        return f'{self.some_number}'

    def __add__(self, other):
        if Cell.__check(other):
            return self.some_number + other.some_number

    def __sub__(self, other):
        """Return result of subtraction if first cell is bigger than second. Otherwise return warning message"""
        if Cell.__check(other):
            res = self.some_number - other.some_number
            if res > 0:
                return res
            else:
                return 'Subcell number of first cell is less than subcell number of second cell'

    def __mul__(self, other):
        if Cell.__check(other):
            return self.some_number * other.some_number

    def __floordiv__(self, other):
        """Return result of integer division of bigger cell divided smaller cell"""
        if Cell.__check(other):
            return max(self.some_number, other.some_number) // min(other.some_number, self.some_number)

    def make_order(self, subcell_number):
        print(' ', 'Order of subcells in cell is:', sep='\n')
        return ''.join(['*' * subcell_number + '\n' for el in range(self.some_number // subcell_number)] + [
            '*' * (self.some_number % subcell_number)])


cell_1 = Cell(18)
cell_2 = Cell(40)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(10))
