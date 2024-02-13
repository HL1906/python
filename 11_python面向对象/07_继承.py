class Ye:
    name = None
    age = None

    def yeye(self):
        print(f"{self.name}, {self.age}")
        print(f"这是父类")


class Son:
    gender = None

    def yeson(self):
        print(f"{self.gender}")
        print(f"这是第二个父类")


# 单继承
class Fu(Ye):
    gender = None

    def baba(self):
        print(self.gender)
        self.yeye()
        print(f"继承了Ye类，是单继承")


# 多继承
class Zi(Ye, Son):
    def son(self):
        print(f"{self.name}, {self.age}, {self.gender}")
        print(f"这里是多继承，继承了Ye和Son类")


print("-------------打印父类信息--------------------")
# 打印父类信息
p1 = Ye()
p1.name = "张三"
p1.age = 23
p1.yeye()

print("-------------打印单继承信息--------------------")

# 打印单继承信息
p2 = Fu()
p2.name = "李四"
p2.age = 24
p2.gender = "女"
p2.baba()

print("-------------打印多继承信息--------------------")
# 打印多继承信息
p3 = Zi()
p3.name = "王五"
p3.age = 25
p3.gender = "女"
p3.son()
