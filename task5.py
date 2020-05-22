from functools import reduce

print(reduce(lambda x, y: x * y, [number for number in range(100, 1001) if number % 2 == 0]))
