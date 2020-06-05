class OwnError(Exception):
    def __init__(self, warning_text):
        """Creates an warning message if exception was happened"""
        self.txt = warning_text


class MyClass:
    def __init__(self):
        self.user_list = []

    def __call__(self, *args, **kwargs):
        """Return list that consists only from numbers"""
        while True:
            user_input = input('Enter some number or str. If you want to finish enter \'stop\': ').strip()
            if user_input == 'stop':
                return self.user_list
                break
            try:
                if not user_input.replace('-', '').replace('.', '').isdigit():
                    raise OwnError('You have to enter only numbers')
            except OwnError as error:
                print(error)
            else:
                self.user_list.append(float(user_input))


some_obj = MyClass()
some_obj()
print(getattr(some_obj, 'user_list'))
