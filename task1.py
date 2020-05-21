from sys import argv

script_name, output, rate, premium = argv


def salary_calc(x, y, z):
    result = int(x) * int(y) + int(z)
    return f'Заработная плата составила {result}'


print(f'При выработке {output} часов, ставке {rate} в час и премии {premium} {salary_calc(output, rate, premium)}')
