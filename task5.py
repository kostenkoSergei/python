proceeds = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))
profit = proceeds - costs
if profit > 0:
    print('Фирма работает с прибылью')
    profitability = profit / proceeds
    print('Рентабельность составила: {:.2f}'.format(profitability))
    number = int(input('Введите число сотрудников фирмы: '))
    print('Прибыль фирмы в расчете на одного сотрудника составит: {:.2f}'.format(profit / number))
elif profit == 0:
    print('Фирма работает в ноль. Издержки равны выручке')
else:
    print('Фирма работет в убыток. Убыток составил: {:.2f}'.format(proceeds - costs))
