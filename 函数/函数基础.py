#函数定义
def space():
    print()
    print('---------------------------')
    print()
    return 1
space()

#函数参数及返回值
def circle_area(r):
    area = 3.14 * r * r
    return area, round(2 * 3.14 * r,2)
c_area = circle_area(10)
print(c_area)
#会返回到元组中
print(type(c_area))

#为了代码的可读性,需加入函数的说明文档,方便理解
#可将鼠标放到函数名上看到函数的说明文档
#可用help查看函数的说明文档
def circle_area_len(r):
    """
    该函数用于根据圆的半径，计算圆的面积和圆的周长
    :param r: 圆的半径                 #描述函数的参数
    :return: 圆的面积，圆的周长         #描述函数的返回值
    #仅在pycharm中有较好的适配
    """
    return 3.14 * r * r, 2 * 3.14 * r
al = circle_area_len(10)
print(al)
#仅在pycharm中有较好适配
help(circle_area_len)

#函数调用遵循栈结构，
#最后被调用的函数最先返回LIFO
# (Last In First Out，后进先出)