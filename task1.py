city = 'Санкт-Петербург'
print(city)
color = 'green'
number = 4
print(str(number), color)
name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
insurance_number = input('Введите номер полиса страхования: ')
age = int(input('Введите Ваш возраст: '))
insurance_period = 10
print(f'{surname} {name}, номер полиса страхования: {insurance_number}')
print(f'Ваш новый полис будет действовать до {age + insurance_period} лет')

