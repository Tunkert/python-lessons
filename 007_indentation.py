# indentation is super important in python
import keyword

is_programmer = True

for number in range(1, 11):
    print(number)
print("Hello")  # this will only print once after the loop is over

if is_programmer:
    print("I am a programmer")
    print("This also runs if 'is_programmer' is True")
else:
    print("Is not a programmer.")

# Talk about how this IDE can write the import statement for you .. nice!
print(keyword.kwlist)  # this gives us a list of reserved keywords which we can't use for variables
