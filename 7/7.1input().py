message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("please enter you name: ")#引号里最后加个空格
print("Hello, " + name + "!")


#创建多行字符串，并引用输入
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "#运算符+=在存储在prompt中的字符串末尾附加一个字符串

name = input(prompt)
print("\nHello, " + name + "!")

#使用 int()来获取数值输入
age=input("How old are you? ")
age=int(age)
print(str(age))

#判断奇偶
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number=int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")