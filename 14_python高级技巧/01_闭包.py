# 简单闭包
# def outer(logo):
#     def inter(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inter
#
#
# fn1 = outer("黑马程序员")
# fn1("大家好")
#
# fn1 = outer("传智教育")
# fn1("大家好")


# 使用nonlocal关键字改外部函数的值
# def outer(num1):
#     def inter(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inter
#
#
# fn = outer(10)
# fn(10)
#  使用闭包实现ATM小案例

def account_create(inital_amount=0):
    def atm(num, deposit=True):
        nonlocal inital_amount
        if deposit:
            inital_amount += num
            print(f"存款, +{num}, 账户余额，{inital_amount}")
        else:
            inital_amount -= num
            print(f"取款, +{num}, 账户余额，{inital_amount}")

    return atm


atm = account_create()

atm(100)
atm(100)
atm(300, deposit=False)
