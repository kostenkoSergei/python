def int_func(word):
    """Возвращает слово с заглавной первой буквой."""
    # проверяем, все ли буквы латинские
    for el in word:
        if ord(el) not in range(61, 123):
            return False
    result = word.title()
    return result


text = input('Ввведите строку из слов, состоящих из маленьких латинских букв, разделенных пробелом: ').lower()


def out_func(some_text):
    """Возвращает исходную строку, где первая буква каждого слова переведена в верхний регистр."""
    lst = []
    for el in text.strip().split():
        if int_func(el):
            lst.append(int_func(el))
    # проверяем, все ли слова прошли проверку на отсутствие не латинских букв
    if len(lst) == len(text.strip().split()):
        return ' '.join(lst)
    else:
        return 'Не все слова во введенном предложении состоят только из латинских букв'


print(out_func(text))
