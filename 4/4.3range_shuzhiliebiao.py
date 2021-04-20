#使用range（）生成一系列数字
for value in list(range(1,6)):
    print(value,end=' ')

print('\n')
#list()可以将range()的结果直接转换为列表
numbers=list(range(1,6))
print(numbers)

#range()可以指定步长
even_numbers=list(range(2,11,2))#最后一个是步长
print(even_numbers)

#range()示例
squares=[]
for value in range(1,11):
    #square=value**2
    #squares.append(square)去掉临时变量square
    squares.append(value**2)

print(squares)

#对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))

#列表解析
sqs=[val**2 for val in range(1,11)]
print(sqs)
