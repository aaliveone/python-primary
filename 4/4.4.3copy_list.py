my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite food are:")
print(friend_foods)