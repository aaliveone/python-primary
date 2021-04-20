where_go = {}

polling_active = True

while polling_active:
    name = input("\nEnter your name: ")
    where = input("If you could visit one place in the world, where would you go? ")

    where_go[name] = where

    repeat = input("yes/no? ")
    if repeat == 'no':
        polling_active = False
for name_user, where_to in where_go.items():
    print(name_user.title() + " want to go " + where_to.title() + ".")