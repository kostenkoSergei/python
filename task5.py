def user_sum():
    result = 0
    while True:
        user_str = input('Введите несколько чисел, разделенных пробелом. Для выхода нажмите "q": ').lower()
        user_lst = []
        if 'q' not in user_str:
            # разделяем строку по пробелу. переводим каждый элемент в int
            for el in map(int, user_str.strip().split()):
                user_lst.append(el)
            result += sum(user_lst)
            print('Сумма чисел равна: ', result)
        else:
            if user_str.strip() == 'q':
                break
            user_str = user_str[:user_str.find('q')].strip()
            for el in map(int, user_str.strip().split()):
                user_lst.append(el)
            result += sum(user_lst)
            break
    return result


print('Итоговая сумма равна: ', user_sum())
