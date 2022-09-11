my_name = "Timothy Unkert"
my_age = 46

# Python 3.6 and later
print(f"My name is {my_name} and I am {my_age} years old.")

# Prior to Python 3.6
print("My name is {} and I am {} years old.".format(my_name, my_age))

my_string = """
My name is {}.
I am {} years old.
"""

print(my_string.format(my_name, my_age))

# We can also do concatenation.

print("My name is " + my_name + " and I am " + str(my_age) + " years old.")
# with this method we have to convert the integer to a string by using str
