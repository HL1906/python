# 设置一个类
class Student:
    name = None
    age = None
    gender = None


# 创建一个对象
stu = Student()
# 对象属性进行赋值
stu.name = "张三"
stu.age = 23
stu.gender = '男'
# 获取对象信息
print(f"name:{stu.name}, age:{stu.age}, gender:{stu.gender}")
