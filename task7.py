def fact(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
        yield result


for el in fact(4):
    print(el)
