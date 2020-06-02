import traceback


class OwnError(ZeroDivisionError):
    def __init__(self, warning_text):
        """Creates an warning message if exception was happened"""
        self.txt = warning_text


user_list = []
while True:
    user_input = input('Enter some number or str. If you want to finish enter \'stop\': ')
    if user_input == 'stop':
        print(user_list)
        break
    try:
        if not user_input.isdigit():
            raise OwnError('You have to enter only numbers')
    except OwnError as error:
        print(error)
    else:
        user_list.append(float(user_input))