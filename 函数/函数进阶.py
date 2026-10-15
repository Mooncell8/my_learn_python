#全局变量和局部变量
#与c相同
pi = 3.14159
def func():
     pi = 3.14
     print(pi)
     return 0
func()
print(pi)

#global关键字,将局部变量变为全局变量
#先声明再使用
pii = 3.1415926
print(pii)
def func():
    global pii
    pii = 3.14
    print(pii)
    return 0
func()
print(pii)

#传参方式
#位置传参,上述方式
#关键字传参,与idl相同
def reg(name,age,city) -> dict[str, int] | None :
    print(f"姓名: {name}, age: {age}, city: {city}")
    return {"姓名": name, "age": age, "city": city}
# stu = reg("淮北" , age = 20 , name = "张三")
#位置参数和关键字参数可以混用,但位置参数必须在前面
#因为位置参数在前面,所以位置参数必须是前n个
#python不会提取剩余的关键字并排序
stu = reg("张三"  , city = "淮北", age = 20)
print(stu)
"""
参数少(不超过3个),且顺序自然可以用位置传参
参数多或易混淆的场景使用关键字参数
"""


#默认参数(缺省参数)
def reg_(name,age,city = "淮北"):
    print(f"姓名: {name}, age: {age}, city: {city}")
    # return {"name": name, "age": age, "city": city}
    return 0
stt = reg_("李四", 19)
print(stt)


#不定长参数
"""
:c语言陋习
时间复杂度+1
def ave(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum/len(args)
"""
#keyword,kw缩写
# 关键字参数,封装为字典型
def data(*args, **kwargs) -> int | float:
    min_data = min(args)
    max_data = max(args)
    ave_data = sum(args) / len(args)

    """
        当传入的值为0时,if代码会判断为false
        导致后面的代码不执行,保留默认的小数位数
        if kwargs.get("round"):
            ave_data = round(ave_data,kwargs.get("round"))
    """
    if kwargs.get("round") is not None:
        ave_data = round(ave_data, kwargs.get("round"))

    print(type(args))
    print(type(kwargs))
    return min_data, max_data, ave_data

data1 = data(10, 20, 30, 40, 5.222, round = 3)
data2 = data(10, 20, 30, 40, 5, round = 3)
#当直接 print(data) 打印一个包含浮点数的元组时
#Python 默认会省略末尾多余的零。
print(data1)
print(data2)


#参数类型(函数作为参数)
# 普通参数：数字、布尔、字符串、列表、元组、集合、字典等。
# 特殊参数：函数。
def add (x, y):
    return x+y
def subtract (x, y):
    return x-y
#计算
def calc(x, y,oper):
    return oper(x, y)
result = calc(10, 20, add)
print(result)


#匿名函数(lambda表达式)
# lambda 参数列表 : 函数体
#只能在一行使用
out_line = lambda : print("----------------------")
print(out_line())
print()
add = lambda x, y : x + y
print(add(10, 20))

data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key = lambda item : len(item))
print(data_list)

data_list.sort(key = len)
print(data_list)

data_list.sort(key = lambda item : len(item), reverse = True)
print(data_list)

"""
建议使用匿名函数的情况：
函数逻辑简单，只在一个地方调用（常作为高阶函数的参数）

建议使用命名函数的情况：
函数逻辑复杂，需要多步操作，
需要多个地方重复使用或需要加文档说明的场景
"""


print(out_line())
#案例(递归)
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)

print(jc(5))
