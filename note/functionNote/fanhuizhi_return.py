#如果调用 len()函数， 并向它传入像'Hello'这样的参数， 函数调用就求值为整数 5
#函数调用求值的结果， 称为函数的“返回值”
#用 def 语句创建函数时， 可以用 return 语句指定应该返回什么值。 return 语句包含以下部分：
# return关键字
# 函数应该返回的值或表达式
#如果在 return 语句中使用了表达式， 返回值就是该表达式求值的结果

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
#因为可以将返回值作为参数传递给另一个函数调用所以可以缩写成一行等价的代码
print(getAnswer(random.randint(1, 9)))
#表达式是值和操作符的组合。函数调用可以用在表达式中， 因为它求值为它的返回值