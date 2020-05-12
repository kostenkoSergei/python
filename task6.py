a = float(input('Введите расстояние, преодоленное в первый день пробежки: '))
b = float(input('Введите желаемый результат преодолеваемого за день расстояния: '))
distance = a
i = 1
while distance < b:
    print('{}-й день: {:.2f}'.format(i, distance))
    distance += distance / 10
    i += 1
print('{}-й день: {:.2f}'.format(i, distance))
print(f'на {i}-й день спортсмен достиг результата — не менее {b} км')
