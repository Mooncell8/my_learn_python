"""
仅第一个 三引号(\""") 会被识别为注释,为灰色
后面的为字符串,为黄色
但是因为只有字符串不影响,所以扔用来表示注释
"""
print("Hello,world")
print("___________")
a = 10
b = 20
c: int = 30#类型注解
names2: list[str | int] = ["A", "C", "E"]
#类型注解只是提示,不会影响程序
a,b,c = c,a,b
print(a,b,c)

#Shift + Enter：快速换行
#Tab / Shift + Tab：缩进或取消缩进
# Ctrl + /：行注释或取消注释（支持多行）
#Shift + F10：运行程序

"""
Ctrl + F：在当前文件中查找。

Ctrl + R：在当前文件中替换。

Ctrl + Shift + F：全局查找。

Ctrl + Shift + R：全局替换。
"""
"""
Shift + F9：启动调试模式。

F8：单步跳过。

F7：单步进入。

Ctrl + F8：设置或取消断点。

Alt + F9：运行到光标处
"""