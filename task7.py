import json

some_dict1 = {}
some_dict2 = {}
general_profit = 0
some_lst = []
count = 0
try:
    with open('file_for_task7_in.txt', 'r', encoding='utf-8') as f:
        for line in f:
            profit = float(line.split()[2]) - float(line.split()[3])
            some_dict1[line.split()[0]] = profit
            if profit >= 0:
                general_profit += profit
                count += 1
        average_profit = round(general_profit / count, 3)
        some_dict2['average_profit'] = average_profit
        some_lst.append(some_dict1)
        some_lst.append(some_dict2)
        print(some_lst)
    with open('file_for_task7_out.json', 'w', encoding='utf-8') as f2:
        json.dump(some_lst, f2, ensure_ascii=False, separators=(',', ': '), indent=4)
    # to check file_for_task7_out.json was written correctly
    with open('file_for_task7_out.json', 'r', encoding='utf-8') as f2:
        print(json.load(f2))
except FileNotFoundError as f:
    print(f)