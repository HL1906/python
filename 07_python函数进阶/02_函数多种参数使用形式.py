"""
演示多种传参数使用形式
"""


def user_info(name, age, gender):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")


# 位置参数 —— 默认使用形成
user_info("张三", 23, "男")

# 关键字参数
user_info(gender="女", age=24, name="李四")
user_info(name="王五", age=25, gender="男")
user_info("赵六", age=26, gender="女")


# 缺省参数  就是添加了默认参数（默认参数必须要放在最后一个参数）
def user_info(name, age, gender="男"):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")


user_info("小帅", 23)
user_info("小美", 23, "女")


# 不定长 —— 位置不定长， *号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")


user_info(1, 2, 3, "小美")


# 不定长 —— 关键字不定长， **号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")


user_info(name="张三", age=23)
