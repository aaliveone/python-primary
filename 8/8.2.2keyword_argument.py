def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


#关键字实参是传递给函数的名称—值对
#关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途
#务必准确地指定函数定义中的形参名
describe_pet(animal_type='hamster', pet_name='harry')