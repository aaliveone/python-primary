#需要检查超过两个的情形
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#代码简化
age_1=12
if age_1<4:
    price=0
elif age_1<18:
    price=5
else:
    price=10
print("Your admission cost is $"+str(price)+".")