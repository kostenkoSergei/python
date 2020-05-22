from itertools import cycle, count
for el in count(3):
    if el > 10:
        break
    print(el, end=' ')
print()

user_lst = ['hello!', 'how', 'are', 'you', '?']
count = 0
for el in cycle(user_lst):
    if count == 20:
        break
    print(el, end=' ')
    count += 1
