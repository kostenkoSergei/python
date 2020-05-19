def my_func(*args):
    """Принимает три аргумента. Возвращает сумму двух наибольших"""
    lst = [*args]
    min_number = min(lst)
    lst.remove(min_number)
    result = sum(lst)
    return result


print('Сумма двух наибольших аргументов равна: {}'.format(my_func(-2, 5, 1)))
