# conditionals can alter the control flow of the program

is_programmer = 0
is_a_boss = False
owns_a_boat = 1

if is_programmer:  # this is an example of a 'truthy'
    print("I'm a programmer.")
else:
    print("I'm not a programmer.")

if is_programmer:
    print("Yeah, I'm a programmer.")
elif is_a_boss:
    print("Yeah, I'm a boss")
elif owns_a_boat:
    print("I own a boat.")
else:
    print("I got nothing going on.")

your_age = 21

if your_age >= 21:
    print("You can enter the club. Bottle full of bub?")
elif your_age >= 18:
    print("You can't enter the club, no bottle full of bub, but you can go off to war!")
else:
    print("You are a minor.")
