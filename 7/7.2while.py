#使用while循环来数数
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
#如果没有可供比较的东西， Python将无法继续运行程序;必须给变量message指定一个初始值
#将变量message的初始值设置为空字符串""，让Python首次执行while代码行时有可供检查的东西
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#使用标志
prompt_1 = "\nTell me something, and I will repeat it back to you:"
prompt_1 += "\nEnter 'quit' to end the program. "

active = True
while active:
    mes = input(prompt_1)

    if mes == 'quit':
        active = False
    else:
        print(mes)