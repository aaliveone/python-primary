def make_pizza(size, *toppings):
    """Variable parameters.可变参数。

    *pama 元组；**pama 字典
    概述要制作的披萨"""
    print("\nMaking a {}"
          "-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print("- " + topping)