lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 5, 10, 7, 4, 11, 5]
new_lst = [lst[i] for i in range(len(lst)) if lst[i] not in lst[i + 1:] and lst[i] not in lst[:i]]
print(new_lst)
