#元组tuple基本操作
#索引与切片操作与列表一致
t1 = (1, 3, 3 , 5, 7, 9)
print(t1)
print(type(t1))
print(t1.index(3))
print(t1.count(3))
print(t1[0],t1[-1])

#切片
print(t1[0:5:1])

#无法直接定义单个元素的元组
#会认为这个是提升优先级的括号
t2 = (100)
print(type(t2))
print(t2)
#需在数字后面加上逗号
t3 = (100,)
print(type(t3))
print(t3)


#不加括号仍是元组,但书写时不推荐
t2 = 1, 2, 3, 4.0
#元组的组包与解包
a, b ,c ,d= t2
print(a, b, c, d)
#*星号可以接受多个值,接收的类型为列表list
#其余值为单个数据的类型
x, *y ,z = t2
print(x, y, z)
print(type(x), type(y), type(z))

#多个数据交换
a = 10
b = 20
print(a, b)
#解包 = 组包
#a, b = (b, a)括号可省略
a, b = b, a
print(a, b)


#嵌套元组
#方式一
tt = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95)
)
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for i in tt:
    total = i[2] + i[3] + i[4]
    ave = total / 3
    #冒号后可以设置格式{ave:.1f}
    print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {ave:.1f}")

#方式二
for id1, name, ch, math, eng in tt:
    total = ch + math + eng
    print(f"{id1} \t {total}")


#获取各科最高分和最低分
ch_scores = [i[2] for i in tt]
math_scores = [i[3] for i in tt]
Eng_scores = [i[4] for i in tt]
print(ch_scores, math_scores, Eng_scores)
print(f"语文最低分:{min(ch_scores)},最高分:{max(ch_scores)},平均分{sum(ch_scores)/len(ch_scores):.2f}")

#查找平均分大于90的学生,并输出
for i in tt:
    total = i[2] + i[3] + i[4]
    ave = total / 3
    if ave > 90:
        print(f"学号:{i[0]},姓名:{i[1]},平均分:{ave:.2f}")

#方式二解包操作实现
for id1, name, ch, math, eng in tt:
    total = ch + math + eng
    ave = total / 3
    if ave > 90:
        print(f"{id1} \t {total}")