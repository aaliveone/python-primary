def describe_pet(pet_name, animal_type='dog'):
    """Show pet information.显示宠物的信息。

    默认宠物为dog，这就是默认值"""
    print("\nI have a " + animal_type + ".")
    print("My {0}'s name is {1}." .format(animal_type,pet_name.title()))

describe_pet(pet_name='willie')