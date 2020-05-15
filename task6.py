# создаем пустой список для структуры Товары
full_product_list = []
# создаем словарь с ключами характеристик товаров
lst_param = ['название', 'цена', 'количество', 'ед.']
user_dict = dict.fromkeys(lst_param)
# cоздаем словарь для аналитики товаров
analytic_dict = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
user_number = int(input('Введите количество товаров, которое хотите добавить: '))
for j in range(1, user_number + 1):
    user_lst = input('Введите название товара, цену, количество и ед. измерения через ",": ')
    user_lst_format = user_lst.replace(' ', '').split(',')
    # приводим к типу int цену и количество
    user_lst_format[1] = int(user_lst_format[1])
    user_lst_format[2] = int(user_lst_format[2])
    i = 0
    # заполняем словарь для структуры Товары
    for el in user_dict:
        user_dict[el] = user_lst_format[i]
        i += 1
    # кортеж для одной позиции товара
    one_item = j, user_dict.copy()
    # добавляем кортеж в структуру Товары
    full_product_list.append(one_item)
    i = 0
    # собираем аналитику о товарах
    for el in analytic_dict:
        if i == 3 and user_lst_format[i] in analytic_dict[el]:  # убираем дублирование для ед.изм.
            i += 1
            continue
        analytic_dict[el].append(user_lst_format[i])
        i += 1

print('Структура "Товары" будет иметь вид: ')
print(full_product_list)
print('Аналитика товаров будет иметь вид: ')
print(analytic_dict)
