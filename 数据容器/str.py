#str基本方法
#字符串切片
s = " Hello World "
print(s[1])
print(s[0:5])
for item in s:
    print(item,end=" ")
print()
#从后往前截取,可以实现字符串倒置
print(s[::-1])

#字符串常用方法
#find()在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1
print(s.find("World"))
#count()统计出现的次数
print(f"l字符在s中出现了{s.count("l")}次")

#upper()转为大写lowe()转为小写
su = s.upper()
print(su)
sl = s.lower()
print(sl)

#split()将字符串按照指定字符串切割
slist = s.split(" ")
print(slist)
print(type(slist))

#strip()去除字符串两端的空格
ss = s.strip()
print(ss)

#replace()将字符串中的指定子串替换为新的内容
sr = s.replace("World","Python")
print(sr)
#starswith()/endswith()判断字符串是否以指定的
#字符串开头/结尾,返回bool值
print(s)
print(s.startswith("World"))


#案例
# 邮箱格式验证：用户输入一个邮箱，
# 验证邮箱格式是否正确(包含一个@和至少一个。)，
# 如果输入正确，输出“邮箱格式正确”，否则输出”邮箱格式错误”。
#接收用户输入的邮箱
mail = input("请输入邮箱:")

#判断邮箱格式
if mail.count("@") == 1 and mail.count(".") >= 1:
    print("邮箱合法")
else:
    print("邮箱非法")

#方式二 in-->判断子串是否在字符串中
if mail.count("@") == 1 and "." in mail:
    print("邮箱合法")
else:
    print("邮箱非法")


#判断字符串是否回文
hw = input("输入回文字符串")
#忽略大小写和空格
hw2 = input("输入回文字符串：").lower().replace(" ", "")
if hw == hw[::-1]:
    print('为回文')
else:
    print("不为回文")
if hw2 == hw2[::-1]:
    print('为回文')
else:
    print("不为回文")

"""
hw = input("输入回文字符串：")
left, right = 0, len(hw) - 1
is_palindrome = True
while left < right:
    if hw[left] != hw[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print('为回文' if is_palindrome else '不是回文')
"""