#if格式
a = int(input("请输入a的值"))
if 20 >= a >= 10:
    print(f"a的值为{a}")
    print("缩进需要固定四格或tab制表符")
elif a >= 20:
    print(f"a的值需要小于20")
else:
    print("a的值需要大于10")
print("如果没有缩进,则会跳出if语句")

#match
#类似于c中的switch
day = input("今天是星期几(1-7)")
match day:
    case "1" if day != "0":
        print("星期一刷剿灭")
    case "2":
        print("星期二下午公休")
    case "3":
        print("承上启下")
    case "4":
        print("疯狂星期四")
    case "5" :
        print("明天不用上课了")
    case "6" | "7":
        print("检查周常任务做完没")
    case _:
        print("你一周有几天?")


print("-----------------------")
i = 2
print(i)
for i in range(7):
    print(i,end = "")
print()
for i in range(7):
    print(i,end = "")
print("也就是说")
print("for循环中的i会自动重置为0")
print(i)
print("for循环的i使用完毕后不会销毁")