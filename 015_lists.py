numbers = [5, 66, 83, 22, 1, 23, 11]

for number in numbers:
    print(number)

my_other_list = ["Hello", True, False, 3.14, 12, (1, 2, 3)]

for stuff in my_other_list:
    print(stuff)

# List Methods
# Pop()
print(my_other_list.pop())  # will print the tuple
print(my_other_list.pop(2))  # will print False

# len
print(len(my_other_list))  # determine the length of the list

print(my_other_list.reverse())  # prints None

print(my_other_list)  # what was left of my list is reversed

print(my_other_list.clear())  # print None

print(my_other_list)  # the list is empty
