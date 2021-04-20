def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


#一旦执行跳到 except 子句的代码， 就不会回到 try 子句。 它会继续照常向下执行。
#如果在 try 子句中的代码导致一个错误，程序执行就立即转到 except 子句的代码。在运行那些代码之后，执行照常继续