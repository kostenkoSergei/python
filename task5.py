previous_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите целое число от 0 до 9: '))
# добавляем элемент пользователя в начальный список нулевым элементом
new_list = [user_number] + previous_list
for i in range(len(new_list) - 1):
    if new_list[i] < new_list[i + 1]:
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
print(new_list)
print('Структура "Рейтинг" будет иметь вид: ', end=' ')
print(*new_list, sep=', ')
