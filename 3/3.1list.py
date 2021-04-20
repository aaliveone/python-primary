bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)#输出整个列表

print(bicycles[0])#访问列表中第一个元素

print(bicycles[1].title())#访问第二个元素比对其内容进行操作

print(bicycles[-1])#不需要知道列表的长度就可以访问列表中最后一个元素

massage="My first bicycle was a " + bicycles[0].title() + "."
    #+连接字符串；这是使用列表中的各个值的示例
print(massage)