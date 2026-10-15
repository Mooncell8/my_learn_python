# 注释要多写
"""
多行注释
用三引号
"""
num = 3.1415
type_num = type(num)
# str_num = (num)
print(type_num)
print(type(num))
print(type(None))
print(type(True))
print(type(10))
print(type("10"))

print("--------------------")

is_int = isinstance(num,int)
print(is_int)
print(type(is_int))
print(isinstance(num,int))

print("--------------------")
#字符串定义
#字符串的使用

str_1 = """三引号字符串
可以换行
单引号和双引号
作用一致
如果在同一个print里,则不会空一行"""
str_2 = """
如果三引号与文字不在一行
则会输出换行(及对应行数的空行)
"""

#转义字符\
# \n为换行符,\t为制表符(TAB)
#值得注意%需要使用%%来进行转义(字符串格式化)
str_3 = "转义字符\\\n换行,\t制表\\n为换行符,\\t为制表符(TAB)"
# 或者如idl,用不同的引号来区分
print(str_1,str_2)
print(str_3)


print("字符串拼接")
#字符串拼接
#可以用+连接
#也可以直接连接
#","+str_4必须要用+连接
# str强制转为字符串类型
str_4 = "world"
print("Hello"","+str_4)
print(str(num))
print(type(str(num)))
print(type(num))
print('-----------')
str(num)
print(type(num))
#str并不改变()内的类型,只作用于当条语句的输出

#字符串格式化
print('-----------------')
print("字符串格式化")
#通过%占位符进行快速拼接
#类似于c语言
s1 = " 来进行 "
print("使用%% %s拼接" % s1)
print(f"目前最常见的,使用f-string{s1}拼接")
print("使用format方法{}拼接".format(s1))

print('-----------------')

#输入与输出
#   s2 = input("输入s2代表的内容")
#   print(s2)
s3="""s2 = input("输入s2代表的内容")
print(s2)
"""