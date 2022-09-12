my_list = [1, 2, 2, 4, 4.5, 6, 7, 8, 10, 11]

my_new_list = my_list[1:5]  # will stop before index 5

print(my_new_list)

my_skip_list = my_list[::2]  # will jump by 2

print(my_skip_list)

my_whole_list = my_list[:]

print(my_whole_list)

my_reverse_list = my_list[::-1]

print(my_reverse_list)
