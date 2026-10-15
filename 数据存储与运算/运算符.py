#+-*/
#加减乘除
#//整除,%取余
#**幂指数
##算术运算符的优先级 --> ** --> * / // % --> + -
print("0.1 + 10 / 4**2 = ", (0.1 + 10) / 4 ** 2)

#x=input("x的值为")
x = "10"
y = "5"
print("x + y = ",x + y)
print("只是字符串的拼接,需要强制转换为int或float")
# x = int(input("请输入x的值: "))
print("x + y = ",int(x) + int(y))

x = 10.0
y = 5.0
print("x - y = ",x - y)
print("如果强制转换会损失精度")

num = 10
print("num =",num)
num += 10
print("num += 2的结果为",num)
num -= 10
num *= 10
num /= 10
num %= 10
num **= 10
num //= 10
print(num)

#比较运算符
#返回为bool类型
print(f"x = {x},y = {y}")
print(x == y)
print(type(x == y))
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#逻辑运算符
#and    or  not
#逻辑与 逻辑或 逻辑非
# 并且  或者  取反
# &&   ||
n = 15
print(f"{n}在10-20之间吗: ", n >= 10 and n <= 20)
print(f"{n}在10-20之间吗: ", 10 <= n <= 20)