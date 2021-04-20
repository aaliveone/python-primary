#存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }

#概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#存储人名和喜爱的语言
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python','haskell'],
    }

for name,languages in favorite_languages.items():

    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite languages is:"
              + languages[0] + ".")
    else:
        print("\n" + name.title() + "'s favorite languages are: ")
        
        for language in languages:
            print("\t" + language.title())