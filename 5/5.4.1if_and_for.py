requested_toppings = ['mushrooms','green peppers','extra cheese']
#requested_toppings=[]

#Python将在列表至少包含一个元素时返回True，并在列表为空时返回False
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping=='green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding "+requested_topping+".")

    print("\nFinished marking your pizza!")
else:
    print("Are you sure you want a plain pizza?")