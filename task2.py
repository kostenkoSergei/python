try:
    with open('file_for_task2.txt', 'r', encoding='utf-8') as f:
        count_string = 1
        for line in f:
            print(f'количество слов в {count_string} строке равно {len(line.split())}')
            count_string += 1
        print(f'Количество строк в файле: {count_string - 1}')
except FileNotFoundError as f:
    print(f)
