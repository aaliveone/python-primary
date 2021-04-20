many = input("How many customers have meals? ")
many = int(many)

if many > 8:
    print("There are no empty tables!")
else:
    print("There are empty tables!")

number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is 10 times.")
else:
    print("The number " + str(number) + " is not 10 times.")