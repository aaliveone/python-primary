digists=list(range(1,10))
print(digists)

for digist in digists:
    if digist==1:
        print(str(digist)+"st")#123是数值格式不是文本-字符串
    elif digist==2:
        print(str(digist)+"nd")
    elif digist==3:
        print(str(digist)+"rd")
    else:
        print(str(digist)+"th")