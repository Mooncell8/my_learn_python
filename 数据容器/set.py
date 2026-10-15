#set集合基本操作
#set是无序的\不可重复的\可修改的
#set会自动去重
s1 = {5, 3, 2, 0, 9 ,12, 43, 64, 22, 5, 0}
#空集合不可用{},{}表示的是字典
#正确定义空集合
s2 = set()
s3 = {}
print(s1)
print(s1)
print(s2)
print(type(s1))
print(type(s2))
print(type(s3))

#set操作
#add()添加元素的集合中
s1.add(1)
print(s1)

#remove()删除指定的元素(不存在将报错)
s1.remove(1)
print(s1)

#pop()随机删除集合中的元素并返回
a = s1.pop()
print(a)
print(s1)

#clear()清空集合
s1.clear()
print(s1)

#difference(）：求两个集合的差集
# 存在于第一个集合，但不存在于第二个集合
s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}
print
print(s2.difference(s3))
print(s3.difference(s2))
#方式二
# - 也可以用来求差集
print(s3 - s2)
#方式三：集合推导式 ---> 快速构建集合
# 语法：{要往集合中添加的数据 for s in set1 if 条件}
f5 = {s for s in s3 if s not in s2}
print(f5)
print("------------")

#union()求两个集合的并集(set会自动去重)
print(s2.union(s3))
#方式二
#用 | 求并集
print(s2 | s3)

#intersection()求两个集合的交集
print(s3.intersection(s2))
# & 也可以用来求交集
s4 = s2 & s3
print(s4)
print(s1.intersection(s2).intersection(s3))