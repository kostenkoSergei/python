with open('file_for_task5.txt', 'w+') as f:
    try:
        f.write(input('Введите набор чисел, разделенных пробелами: '))
        f.seek(0)
        lst = list(map(float, f.read().split()))
        print(f'Сумма введенных чисел составила: {sum(lst)}')
    except ValueError as v:
        print(v)

