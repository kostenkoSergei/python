import traceback


class OwnError(ZeroDivisionError):
    def __init__(self, warning_text):
        """Creates an warning message if exception was happened"""
        self.txt = warning_text


class MyClass:
    def __call__(self, x, y):
        return round(x / y, 2)


try:
    some_obj = MyClass()
    some_obj.x = float(input('Enter first number: '))
    some_obj.y = float(input('Enter second number: '))
    if some_obj.y == 0:
        raise OwnError('Division dy zero is prohibited. You have to go to math class again')
except OwnError as error:
    print(error)
except ValueError:
    print('You entered not a number,', '\n', traceback.format_exc())
else:
    print(f'Your result is {some_obj(some_obj.x, some_obj.y)}')
