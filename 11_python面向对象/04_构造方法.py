# 构造方法
# 空参和带参构造方法不能同时存在
# 格式：__init__()

class Student:
    name = None
    age = None
    gender = None

    # # 相当于Java中的空参构造
    # def __init__(self):
    #     print("这是空参构造")

# 相当于Java中的带参构造
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("这是带参构造")
        print(f"name:{self.name}, age:{self.age}, gender:{self.gender}")


# stu1 = Student()
stu2 = Student("张三", 23, "男")

