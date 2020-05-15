user_str = input('Введите строку из нескольких слов, разделенных пробелами: ')
for ind, el in enumerate(user_str.split(' '), 1):
    print(ind, el[:10])



