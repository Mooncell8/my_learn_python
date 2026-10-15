#教务管理系统
#添加学生成绩
#修改学生成绩
#删除学生成绩
#查询学生成绩
#展示全部学生成绩


#学生类
class Stu:
    def __init__(self,name,chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}|总分:{self.chinese+self.math+self.english}"

    #修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english



#教务管理系统
class EduMannagement:
    system_version = "1.0"
    system_name = "EduManagement"

    def __init__(self):
        self.student_list = []#列表:记录学生成绩

    def add_student(self):#添加学生成绩
        name = input("请输入学生姓名:")


        for s  in  self.student_list:
            if s.name == name:
                print("学生已存在")
                return

        chinese = int(input("请输入语文成绩:"))
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Stu(name, chinese , math, english)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("成绩不合格式(0-100)")

    #修改学生姓名
    def update_score(self):
        name = input("请输入学生姓名:")

        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩为:{s}")

                while True:
                    chinese = int(input("请输入修改后的语文成绩:"))
                    math = int(input("请输入修改后的数学成绩:"))
                    english = int(input("请输入修改后的英语成绩:"))

                    if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                        s.update_score(chinese, math, english)
                        print("成绩修改成功")
                        print(f"当前成绩为:{s}")
                        print()
                        return
                    else:
                        print("成绩不合格式(0-100),请重新输入")



        print("未找到该学生")


    def del_student(self):#删除学生成绩
        name = input("请输入学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("未找到该学生")

    #查找指定学生
    def query_student(self):
        name = input("请输入学生姓名:")

        for s in self.student_list:
            if s.name == name:
                print(f"学生成绩为:{s}")
                return
        print("未找到学生")

    #输出全部学生信息
    def print_students(self):
        for s in self.student_list:
            print(s)


    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduMannagement.system_version}")
        while True:
            print()
            print("###################################################################")
            print("1.添加学生  2.修改学生  3.删除学生  4.查找指定学生  5.全部学生信息  6.退出系统")
            print("###################################################################")
            print()

            choice = input("请选择要执行的操作(1-6)")
            try:
                match choice:
                    case "1":#添加学生
                        self.add_student()
                    case "2":#修改学生
                        self.update_score()
                    case "3":#删除学生
                        self.del_student()
                    case "4":#查找指定学生
                        self.query_student()
                    case "5":#全部学生信息
                        self.print_students()
                    case "6":#退出
                        print("退出成功")
                        break
                    case _:
                        print("输入错误,请重新选择1-6,仅输入数字")
            except ValueError as e:
                print("输入的数据有问题,请检查后重新输入,错误信息:",e)
            except Exception as e:
                print("程序运行出错了,请重新选择,错误信息:",e)


#测试
if __name__ == "__main__":
    edu_management = EduMannagement()
    edu_management.run()