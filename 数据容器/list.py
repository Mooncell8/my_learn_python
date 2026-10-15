#列表定义
s = [1, 2, 3, 4, True, "可以混杂", "但是一般不这么做", 8, 9]
print(s[0],s[-1])#正向索引,从0开始,反向索引,从-1开始
print(s[5],s[6])
s[4] = False
print(s)
del s[8]
print(s)
for item in s:
    print(item,end=" ")

#列表的切片
print("序列数据[开始索引:结束索引:步长]")
print("不包含结束索引,步长默认为1")
print(s[:2])
print(s[2:])
print(type(s[:2:]))
print(s[0:-5])

#list常用方法

#列表末尾添加元素
s.append(10)
print(s)

#在索引前插入元素
s.insert(8,9)
print(s)

#移除第一个匹配的元素
s.remove(10)
print(s)

#删除索引对应的元素,可以用变量接收
#如果没有指定索引,则删除最后一个
e = s.pop(8)
print(s)
s.pop()
s.pop()
s.pop()
s.sort()
#排序
print("如果str和int混杂,则会报错,bool类型不会报错")
print(s)
#反转列表元素
s.reverse()
print(s)
s.pop()

#求和sum()
#获取长度
print(sum(s))
print(sum(s)/len(s))


print("-----------------")
s2 = [1,2,3,4,5,6,7,8,9]
#合并列表
for item in s2:
    s.append(item)#不能s.append(s2)因为括号内应为int
print(s)
#简化
#解包:将列表这一类容器解开成一个一个独立的元素
#组包:将多个值合并到一个容器
new = [*s, *s2]
print(f"简化后new可直接为{new}")
#更加简化
new2 = s + s2
print(f"更加简化后new2为{new2}")
#去除重复的元素
new_s=[]
#实验失败产物,c带来的恶疾
"""
s.sort()
for item in s:
    if s[item] == s[item-1]:
        continue
    new_s.append(item)
print(new_s)
"""

# 两种写法,哪个更好
for item in s:
    if item not in new_s:
        new_s.append(item)
print(f"最终new_s为{new_s}")
# for item in s:
#     if item  in new_s:
#         continue
#     new_s.append(item)
# print(new_s)
"""哪个更好？→ 写法一更好
理由如下：
① 可读性更高（核心原因）
写法一的意图一目了然：“不重复才加入”。
写法二需要读者在脑中做一次逻辑转换：“跳过已存在的 → 剩下的才加入”，多了一层间接推理。
📌 编程原则：代码是写给人看的。减少认知负担 = 更好的代码。
② 更简洁
写法一少了一行 continue，结构更扁平，没有不必要的控制流跳转。
③ continue 的滥用
continue 适合用于复杂循环体中提前跳过某些迭代的场景。在这里，循环体本身只有两行，用 continue 反而显得“杀鸡用牛刀”，增加了阅读成本。"""
# new_s = list(dict.fromkeys(s))
# print(new_s)

#列表推导式
new_list = [i**2 for i in range(1,31) if i % 2 == 0]
print(new_list)

