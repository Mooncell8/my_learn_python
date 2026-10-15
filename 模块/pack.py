#导入模块
""""""
from my_fun import *

"""
import my_fun

print(my_fun.PI)
print(my_fun.NAME)

my_fun.log_separator1()
my_fun.log_separator2()
"""


"""
#导入模块中的功能
from my_fun import log_separator1,log_separator3,PI

print(PI)
print(NAME)   报错
log_separator1()
"""



"""
from my_fun import *

print(PI)
print(my_fun.PI)        #不用加前缀,会报错
print(log_separator2)   #报错
"""