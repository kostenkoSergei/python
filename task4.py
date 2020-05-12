user_number = int(input('Введите целое положительное число: '))
temp = 0
while user_number > 0:
    if user_number % 10 > temp:
        temp = user_number % 10
    if temp == 9:
        break
    user_number = user_number // 10
print('Самая большая цифра во введенном числе: ', temp)

