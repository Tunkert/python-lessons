my_name = "Timothy Unkert"

# methods for use with a string

print(my_name.upper())  # TIMOTHY UNKERT
print(my_name.lower())  # timothy unkert
print(my_name.replace('T', 'B'))
print(my_name.islower())  # False
print(my_name.isalpha())  # False
print(my_name.isnumeric())  # False
print(my_name.istitle())  # True
print(len(my_name))  # 14 - number of characters in the string including the space
# print(my_name == "Timothy unkert")  # False - case sensitive
# print(my_name == "Timothy Unkert")  # True

print(my_name.split(" "))  # prints a list split by the space
print("Timothy" in my_name)  # True

my_multi_line_str = "Once upon a time, " \
    "I went to the store and bought " \
    "a can of beans."

print(my_multi_line_str)

# This can help you avoid long lines.

# If I want lines that go over multiple lines I can do the following
my_real_multiline_str = "I went to the store.\nI then bought some beans.\nThat is my cool story.\nFin."
print(my_real_multiline_str)

# You can also do the following
my_ultra_long_string = """
I went to the store.
I bought some beans.
I also bought hot dogs.
Then I bought macaroni salad.
Then I went home.
The end.
"""

print(my_ultra_long_string)