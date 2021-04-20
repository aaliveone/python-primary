prompt = "\nEnter your age: "

active = True
while active:
    old = input(prompt)
    old = int(old)
    if old < 3 and old >= 0:
        print("Free!")
    elif old < 12:
        print("Your ticket price is $10.")
    elif old < 135:
        print("Your ticket price is $15.")
    else:
        active = False

