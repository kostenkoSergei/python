some_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
f2 = open('file_for_task4_out.txt', 'w', encoding='utf-8')
try:
    with open('file_for_task4_in.txt', 'r') as f1:
        for line in f1:
            word = line.replace(' ', '').split('-')
            f2.writelines(some_dict[word[0]] + ' - ' + word[1])
    f2.close()
except FileNotFoundError as f:
    print(f)
