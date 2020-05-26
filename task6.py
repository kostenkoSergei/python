some_dict = {}
try:
    with open('file_for_task6.txt', 'r', encoding='utf-8') as f:
        for line in f:
            temp_str = ''
            for el in line:
                if el.isdigit():
                    temp_str += el
                else:
                    temp_str += ' '
            lst_digs = list(map(int, temp_str.split()))
            some_dict[line[:line.index(' ') - 1]] = sum(lst_digs)
    print(some_dict)
except FileNotFoundError as f:
    print(f)