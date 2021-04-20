#大多数参数是由它们在函数调用中的位置来识别的.例如， random.randint(1, 10)与 random.randint(10, 1)不同。
#函数调用 random.randint(1, 10)将返回 1 到 10 之间的一个随机整数，因为第一个参数是范围的下界，第二个参数是范围的上界
#而random.randint(10, 1)会导致错误）
#“关键字参数” 是由函数调用时加在它们前面的关键字来识别的。
#关键字参数通常用于可选变元。例如， print()函数有可选的变元 end 和 sep， 分别指定在参数末尾打印什么，以及在参数之间打印什么来隔开它们
print('Hello')
print('World')
#这两个字符串出现在独立的两行中，因为 print()函数自动在传入的字符串末尾添加了换行符
#可以设置 end 关键字参数，将它变成另一个字符串
print('Hello', end='')#end里为空字符串，连空格也没有
print('World')

#如果向 print()传入多个字符串值，该函数就会自动用一个空格分隔他们
print('cats', 'dogs', 'mice')

print('cats', 'dogs', 'mice', sep=',')#sep替换掉默认的分隔字符串
