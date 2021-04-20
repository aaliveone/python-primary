class Car():
    """Create a class about car.创建一个汽车信息的类。

    一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year,odometer_reading=0):
        """初始化描述汽车属性"""

        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = odometer_reading
        #在方法__init__（）内指定初始值（设定默认值）；如果对某个属性设定了默认值，就无需包含为他提供初始值的形参


    def get_descriptive_name(self):
        """返回整洁的描述性信息"""

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""

    print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car=Car('audi','a4',1996)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()