user_list = []
while True:
    el = input('Введите элемент для списка. Если элементов достаточно, наберите стоп: ')
    if el == 'стоп':
        break
    user_list.append(el)
print(user_list)
i = 0
j = 1
while j <= len(user_list) // 2:
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i += 2
    j += 1
print(user_list)

