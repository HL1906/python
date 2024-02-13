class Student:
    name = None
    age = None
    gender = None

    # 成员方法
    def learn(self):
        print(f"{self.name}正在学习！")

    def learn1(self, mgs):
        print(f"{self.name}正在学习！{mgs}")


# 创建对象
stu = Student()
stu.name = "李四"
stu.age = 24
stu.gender = "女"
print(f"name:{stu.name}, age:{stu.age}, gender:{stu.gender}")
stu.learn()
stu.learn1("小声点")
