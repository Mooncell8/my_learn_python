a=5
# stop = 2
# stop = -1
stop = -2
while a >= 0:#条件表达式的结果为布尔类型
    print(a)
    a -= 1
    if a == stop:
        print("stop")
        print("break跳出循环后else语句将不会执行")
        break
else:
    print("循环正常结束")

#1-100累加
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

#for循环
i = 0
sum = 0
for num in range(101):
    sum += num
    i += 1
print(sum)


msg = "Hello World!"
for letter in msg:
    print(letter)
else:
    print("循环结束")

for i in range(1, 10, 2):
    print(i)
print("range函数,(start, end, step)")
for i in range(1, 9, 2):
    print(i)
print("注意不含end")

#嵌套循环
m = 8
n = 6
print("print语句自带换行")
print("在后面加上,end = \"\"")
for j in range(n):
    for i in range(m):
        print("*", end = "   ")
    print()


#打印9x9乘法表
a = 1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {j * i}", end = "\t")
    print()
    a += 1

#import导入库
#random随机数
import random
random_number = random.randint(1,100)
while True:
    print(random_number)
    guess = int(input("请输入一个数字捏"))
    if guess < random_number:
        print("输入的数字小了")
    elif guess > random_number:
        print("输入的数字大了")
    else:
        print("输入的数字对了!!")
        break
