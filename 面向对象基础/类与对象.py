"""
类名的命名规范,遵循大驼峰命名法
每个单词的首字母都是大写
单词之间没有分隔符
class 类名:
    pass

对象名 = 类名()
对象名.属性名 = 属性值
__dict__是Python中用户自定义类实例的一个特殊属性
用于以字典形式存储对象的属性。
"""

class Car:
    pass
#不推荐 动态的为对象添加属性
c1 = Car()
c1.color = 'red'
c1.price = 500

print(c1)
print(c1.color)
print(c1.__dict__)


class Car:
    #类属性: 类属性是属于类本身的属性,
    #所有实例共享的。(所有对象共享的数据或配置)
    wheel = 4   #轮胎数量
    tax_rate = 0.1  #购置税

    #通过实例查找属性时, 会先查找实例属性,
    #实例属性不存在时, 再查找类属性。

    def __init__(self, c_color, c_name, c_price):
        #定义在类中的函数称之为方法
        #__init__初始化方法,对象创建后自动调用,
        #主要用于设置对象的初始状态(设置对象属性)
        # self: 方法的第一个参数, 表示当前创建的实例对象

        #实例属性:实例属性属于每个具体对象的属性
        #每个对象都是独立的。(各个对象特有的数据)
        self.color = c_color
        self.name = c_name
        self.price = c_price
        print("初始化完毕,对象属性已添加")

#定义实例方法
    def running(self):
        print(f"{self.name}滴滴的跑")

    def total_cost(self,discount, rate=0.1):
        """
        计算提车的总费用,包含车的价格和税费
        :param self:
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的最后价格
        """
        total_cost = self.price * discount + rate * self.price
        return total_cost


#魔法方法
    def __str__(self):
        return f"{self.color} {self.name} {self.price}"
    def __eq__(self, other):
        return self.color == other.color and self.price == other.price and  self.name == other.name
    def __lt__(self, other):
        return self.price < other.price

c1 = Car("red", "BMW", 5000)
print(c1.__dict__)


#实例方法
c1.running()

total = c1.total_cost(0.9, 0.3)
print("提车的总费用为", total)


#魔法方法,不需要我们手动调用,会在合适的时机自动调用
"""
__init__            初始化方法
__str__             字符串表示的方法
__eq__              比较两个对象是否相等
__lt/le/gt/ge__     比较两个对象的大小(类似于idl)   
"""

c2 = Car("red", "BMW", 5000)
print(c1.__dict__)
print(c2.__dict__)
print(c2)
print(c1 == c2)#默认对比的是对象的地址

print(c1.__dict__)
print(c1.tax_rate)
print(c1.wheel)
print(Car.wheel)
