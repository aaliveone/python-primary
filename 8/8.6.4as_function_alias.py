#如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名——函数的另一个名称，类似于外号。
#关键字as将函数重命名为你提供的别名
#指定别名的通用语法如下：
#from module_name import function_name as fn
from module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')