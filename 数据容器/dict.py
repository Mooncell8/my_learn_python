#dict字典
#每个字,词对应一个解释,且字或词不能重复
#存储的是键值对(key: value)类型的数据,
#可以根据键(key)找到对应的值(value)
dict1 = {"王林":675,"李慕婉":608,"许立国":478}
print(dict1)
print(type(dict1))

#空字典
dict2 = {}#dict2 = dict()

#访问字典
score = dict1["王林"]
print(score)
print(type(score))
#字典的value可以修改
dict1["王林"] = 688
print(dict1)

#字典的添加
dict1["裴泓"] = 211
print(dict1)

#删除
sc1 = dict1.pop("李慕婉")
print(sc1)
print(dict1)
del dict1["许立国"]

#查询
print(dict1["裴泓"])
print(dict1.get("裴泓"))

#获取字典中的所有的key/value/items
print(dict1.keys())
print(type(dict1.keys()))
print(dict1.values())
print(type(dict1.values()))
print(dict1.items())
print(type(dict1.items()))

#遍历字典
for k, v in dict1.items():
    print(k, v)
for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)