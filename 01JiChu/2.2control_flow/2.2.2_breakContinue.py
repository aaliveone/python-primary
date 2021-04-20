#break 语句用以中断（ Break） 循环语句， 也就是中止循环语句的执行， 即使循环条件没有变更为 False ， 或队列中的项目尚未完全迭代依旧如此

#continue 语句用以告诉 Python 跳过当前循环块中的剩余语句， 并继续该循环的下一次迭代
while True:
    s=input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        print('Too small!')
        continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理