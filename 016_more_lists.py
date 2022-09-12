matrix_list = [
    [1, 2, 3],
    [4, 5],
    [7, 8, 9, 10]
]

print(matrix_list[0][-1])  # prints 3

print(len(matrix_list[1]))  # prints 2

matrix_list.append([1, 2, 3])

print(matrix_list)

print([1, 2, 3] in matrix_list)  # True

matrix_list.remove([4, 5])

print(matrix_list)

matrix_list.remove([1, 2, 3])  # removes first instance

print(matrix_list)
