def user_div(a, b):
    """Возвращает округленный до двух знаков результат деления чисел."""
    try:
        result = round(a / b, 2)
    except ZeroDivisionError as z:
        result = z
    return result


print(user_div(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
