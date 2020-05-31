class Matrix:
    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        return '\n'.join('  '.join(map(lambda x: str(x).rjust(3).center(4), i)) for i in self.some_list)

    def __add__(self, other):
        if len(self.some_list) != len(other.some_list):
            return print('You can summarize only matrixes that have identical sizes')
        self.result = self.some_list.copy()
        for outer_lst1, outer_lst2 in zip(self.result, other.some_list):
            pos = 0
            for i, j in zip(outer_lst1, outer_lst2):
                outer_lst1[pos] = sum([i, j])
                pos += 1
        print('Result of summation of two matrixes:')
        return self.result


user_matrix1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
user_matrix2 = Matrix([[1, 5, 10], [-1, -4, 0], [-1, -34, -5]])
print(user_matrix1)
print()
print(user_matrix2)
print()
try:
    print(Matrix(user_matrix1 + user_matrix2))
except TypeError as t:
    print(t)
