prompt = "\nPlease input pizza ingredients: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("We're going to add " + message + " to the pizza.")