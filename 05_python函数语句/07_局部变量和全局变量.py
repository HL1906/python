# 演示局部变量
print("---------局部变量-----------")


def test_a():
    num = 100
    print(f"test_a:{num}")


# num属于局部变量


test_a() # 100

print("---------全局变量-----------")
# 全局变量
number = 200


def test_b():
    print(f"test_b:{number}")


# number 为全局变量


test_b()# 200
print(number)# 200

print("---------函数内部修改全局变量(global)-----------")
number1 = 200


def test_c():
    print(f"test_c:{number1}")


def test_C():
    global number1  # 设置内部定义的变量为全局变量
    number1 = 500
    print(f"test_C:{number1}")# 500


test_c()# 200
test_C()# 500
print(number1)# 500
