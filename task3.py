try:
    with open('file_for_task3.txt', 'r', encoding='utf') as f:
        low_paid = []
        salaries = []
        for line in f:
            salaries.append(float(line.split()[1]))
            if float(line.split()[1]) < 20:
                low_paid.append(line.split()[0])
        print(low_paid)
        print(f'Cредняя величина заработной платы: {round(sum(salaries) / len(salaries), 3)}')
except FileNotFoundError as f:
    print(f)
