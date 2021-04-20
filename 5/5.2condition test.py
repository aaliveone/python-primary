car='bmw'
print(car=='bmw')

car_1='audi'
print(car_1=='bmw')

car_2='Audi'
print(car_2=='audi')#两个大小写不同的值会被视为不相等

print(car_2.lower()=='audi')

#检查是否不相等
requested_topping = 'mushrooms'

if requested_topping!='anchovies':
    print("Hold the anchovies")

#比较数字
age=18
print(age==18)

answer=17

if answer!=18:
    print("That is not the correct answer. Please try again!")

print(age<21)
print(age<=22)
print(age>33)
print(age>=33)

a=4
b=7
print(a>=5 and b>=5)
print(a>=4 or b>=5)

#检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

#检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")
#布尔表达式，True or False