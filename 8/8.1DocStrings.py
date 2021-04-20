# 函数定义，def关键字定义函数
def greet_user():
    # 紧跟在def greet_user():后面的所有缩进行构成了函数体
    # 文档字符串Documentation Strings 简称DocStrings，这是一种注释，Python使用三引号来生成有关程序中函数的文档
    # 其中第一行以某一大写字母开始， 以句号结束。
    # 第二行为空行， 后跟的第三行开始是任何详细的解释说明
    """"Show simple greetings.显示简单的问候语。

    其中第一行以某一大写字母开始， 以句号结束。第二行为空行， 后跟的第三行开始是任何详细的解释说明.
    DocStrings这是一个范例.通过使用函数的 __doc__ （ 注意其中的双下划綫） 属性（ 属于函数的名称）
    来获取函数 greet_user 的文档字符串属性
     Python 的 help() 函数做的便是获取函数的 __doc__ 属性并以一种整洁的方式将其呈现给你"""
    # 代码行
    print("Hello!")

greet_user()

# 变量username是一个形参——函数完成其工作所需的一项信息。
def greet_users(username):
    """显示问候语"""
    print("Hello, " + username.title() + ".")

#值'jesse'是一个实参，参是调用函数时传递给函数的信息。
greet_users('sss')

help(greet_user)