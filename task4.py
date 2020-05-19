user_number1 = int(input('Введите действительное положительное число, x = '))
user_number2 = int(input('Введите целое отрицательное число, y = '))


# первый вариант реализации: через **
def my_func1(x, y):
    if user_number1 <= 0:
        return 'Не выполнено условие при вводе: х не может быть < или равен 0'
    if user_number2 >= 0:
        return 'Не выполнено условие при вводе: y не может быть > или равен 0'
    else:
        return round(x ** y, 6)


# второй вариант реализации: через цикл
def my_func2(x, y):
    if user_number1 <= 0:
        return 'Не выполнено условие при вводе: х не может быть < или равен 0'
    if user_number2 >= 0:
        return 'Не выполнено условие при вводе: y не может быть > или равен 0'
    else:
        result = 1
        for i in range(-y):
            result *= 1 / x
        return round(result, 6)


print(f'Рузультат возведения x в степень y: {my_func1(user_number1, user_number2)}')
print(f'Рузультат возведения x в степень y: {my_func2(user_number1, user_number2)}')
