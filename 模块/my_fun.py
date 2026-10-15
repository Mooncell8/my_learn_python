# __all__是一个模块级别的特殊变量,
#用于指定 from 模块名 import *时会导入哪些功能(*通配了哪些功能)。
#如果不设置,则其他文件输入*时默认为全部
__all__ = ['PI',"NAME"]


#常量,不会发生变化的数据;常量的名称为全部大写
#实际可以修改,但不会进行修改
PI = 3.1415926
NAME = "Mooncell"


def log_separator1():
    print("- " * 30)#"- "重复输出三十次

def log_separator2( ):
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

#__name__
#python中的内置变量,表示的当前模块的名字
#直接运行当前模块,__name__的值为"__main__"
#当该模块被导入时,__name__的值就是模块名

#执行当前文件,则会执行如下代码;如果被当作模块导入,如下代码不执行
if __name__ == '__main__':
    print(__name__)
    log_separator1()