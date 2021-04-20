#仅适合用于只有一个条件满足的情况:遇到通过了的测试后，Python就跳过余下的测试
age=12
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
#else:
elif age>=65:#else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行,这可能会引入无效甚至恶意的数据
    price=5
print("Your admission cost is $"+str(price)+".")