#创建类
class Dog():#定义了一个名为Dog的类
    #根据约定，在Python首字母大写的名称指的是类。
    #类定义中的括号是空的，因为我们要从空白创建这个类。
    """Create class.创建类。

    一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        #双下划线也是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
        """Method.方法。

        类（class）中的函数叫方法（method）,唯一的不同在于方法拥有一个额外的self的变量
        初始化属性name和age"""
        #self.name = name获取存储在形参name中的值，并将其存储到变量name中，然后该变量被关联到当前创建的实例
        self.name=name
        self.age=age

    def sit(self):
        """Method.坐的方法。

        方法可能不需要参数，但是依旧在函数定义中拥有self变量
        模拟小狗被命令时蹲下"""
        print("{} is now sitting.".format(self.name.title()))

    def roll_over(self):
        """Method.方法。

        模拟小狗被命令时打滚"""
        print("{} rolled over!".format(self.name.title()))

#根据类创建实例
my_dog=Dog('wille',6)#使用实参'willie'和6调用Dog类中的方法__init__()
# 方法__init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例
#将这个实例存储在变量my_dog中

#约定：首字母大写的名称（如Dog）指的是类，而小写的名称（如my_dog）指的是根据类创建的实例

#访问实例的属性——my_dog.name
print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(my_dog.age))

#调用实例
my_dog.sit()
my_dog.roll_over()

#创建多个实例
your_dog=Dog('lucy',3)

print(your_dog.name.title())

your_dog.sit()