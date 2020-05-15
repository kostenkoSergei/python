user_request = int(input('Введите месяц в виде целого числа от 1 до 12: '))
lst_months = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
dict_months = {'зима': [12, 2, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for el in lst_months:
    if user_request in el:
        print(f'Этот месяц относится к сезону: {el[0]}')

for el in dict_months:
    if user_request in dict_months[el]:
        print(f'Этот месяц относится к сезону: {el}')
