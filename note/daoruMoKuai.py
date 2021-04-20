#在代码中 ，import语句包含以下部分：
# import关键字
# 模块的名称（ex：random, sys, os, math）
# 可选的更多模块名称，之间用逗号隔开
import random

for i in range(5):
    #random.randint()函数调用求值为传递给它的两个整数之间的一个随机整数
    #因为 randint()属于 random 模块， 必须在函数名称之前先加上 random.告诉 python 在random 模块中寻找这个函数
    print(random.randint(1, 10))
#import sys
#sys.exit() 该函数得到exit 才执行 退出程序 的命令。