"""
__init__   用于构造方法
__str__    用于实现对象转字符串
__lt__     用于对比两类对象的大小
__le__     用于对比两类对象的小于等于或者大于等于
__eq__     用于2个对象进行相等比较
"""


class Student:
    name = None
    age = None
    gender = None

# __init__构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# __str__变字符串   如果没有这个方法，打印出来的就是地址值
    def __str__(self):
        return f"Student类对象，name:{self.name}, age:{self.age}, gender:{self.gender}"
    print("你好")

# 比较大小

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("张三", 23, "男")
stu2 = Student("李四", 24, "女")
print(stu1)
print(stu2)
print(f"Student类对象，name:{stu1.name}, age:{stu1.age}, gender:{stu1.gender}")  # 或者要这样打印

print(stu1 < stu2)
print(stu1 > stu2)
print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 == stu2)


