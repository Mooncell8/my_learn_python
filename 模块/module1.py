#Python模块(module)：
# 一个.py文件就是一个模块，模块是Python程序的基本组织单位。
# 在模块中可以定义变量、函数、类，以及可执行的代码。
"""
内置模块
math(数学计算)      random(随机数)
os(操作系统)        sys(系统参数)
detetime(日期时间)  time(时间访问)
re(正则)            csv(csv文件操作)
"""

#导入模块   未使用的为灰色
#import 模块名
import random
for i in range(10):
    print(random.randint(1,100), end = " ")

print()
print("------------------------------------------")
#import 模块名 as 别名
import random as rd
for i in range(10):
    print(rd.randint(1,100), end = " ")

print()
print("------------------------------------------")
#from 模块名 import 功能名
from random import randint
for i in range(10):
    print(randint(1,100), end = " ")

print()
print("------------------------------------------")
# from 模块名 import  功能名 as 别名
from random import random as rnd
for i in range(10):
    print(rd.randint(1,100), end = " ")

print()
print("------------------------------------------")
# from 模块名 import *
from random import *
for i in range(10):
    print(randint(1,100), end = " ")

#一般导入文件放到最上面
