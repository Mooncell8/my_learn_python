#此文件想要运行
# 必须在当前上一级目录下的包文件
#如果不在一个文件下,则需要在前面加上 上一级目录 的名字
#绝对路径
# from 模块.utils.func import log_separator1, log_separator3

#一般都为英文名字


# from 包名.模块名
# from 包名 import 模块名

#导入所有模块
#如果导入包,则必须要设置__all__
from utiles import *
print(func.PI)


#导入模块中的功能
#相对路径
from utiles.func import log_separator3
log_separator3()

