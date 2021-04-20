#format（）格式化方法

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#一个字符串可以使用某些特定的格式（ Specification） ， 随后， format 方法将被调用， 使用这一方法中与之相应的参数替换这些格式
#{0} 对应的是格式化方法中的第一个参数，{1}对应第二个参数，python的索引是从0开始的
#数字只是一个可选选项

age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
#这样做同样能得到与前面的程序一样的输出结果

#Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本， 并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))