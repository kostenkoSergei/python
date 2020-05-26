# add some information to file
with open('file_for_task1.txt', 'w', encoding='utf-8') as f:
    while True:
        user_string = input('Введите строку: ')
        if user_string:
            f.writelines(user_string + '\n')
        else:
            break
# read file string by string to check
try:
    with open('file_for_task1.txt', 'r', encoding='utf-8') as f:
        for some_line in f:
            print(some_line, end='')
except FileNotFoundError as f:
    print(f)