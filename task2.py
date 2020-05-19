def get_user_data(var_1, var_2, var_3, var_4, var_5, var_6):
    """Возвращает данные пользователя в виде строки."""
    return f'{var_1} {var_2} {var_3} {var_4} {var_5} {var_6}'


user_name = input('Введите Ваше имя: ')
user_surname = input('Введите Вашу фамилию: ')
user_year_of_birth = input('Введите год Вашего рождения: ')
user_city = input('Введите город проживания: ')
user_email = input('Введите Ваш e-mail: ')
user_phone_number = input('Введите Ваше телефонный номер: ')
print(get_user_data(var_1=user_name, var_2=user_surname, var_3=user_year_of_birth, var_4=user_city, var_5=user_email, var_6=user_phone_number))