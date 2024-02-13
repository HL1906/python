"""
演示函数综合案例开发
"""

# 定义全局变量money name
money = float(500000)
# name = None

# 要求客户输入姓名
name = input("请输入您的姓名")


# 定义查询函数
def query_money():
    print("--------查询余额--------")
    print(f"{name},您好，您的余额为：{money}元")


# 定义存款函数
def save_money():
    print("--------存款--------")
    num1 = float(input("请输入您需要存储的余额："))
    if num1 <= 0:
        print("对不起，存款失败，请正确输入您需要取款的余额。")
    else:
        global money
        money += num1
        print(f"{name}您好，您存款{num1}元成功。\t您当前的余额为：{money}元")


# 定义取款函数
def get_money():
    print("--------取款--------")
    num2 = float(input("请输入您需要取出的余额："))
    global money
    if num2 > money:
        print("对不起，您的余额不足，取款失败。")
    elif num2 < 0:
        print("对不起，请正确输入您的余额。")
    else:
        money -= num2
        print(f"{name}您好，您取款{num2}元成功。\t您当前的剩余余额为：{money}元")


# 定义主菜单函数
def menu():
    print("--------主菜单--------")
    print(f"{name}您好，欢迎来到黑马银行ATM，请选择你的操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")


# 设置无限循环，确保程序不退出
while True:
    menu()
    num = int(input("请开始您的操作:"))
    if num == 1:
        query_money()
    elif num == 2:
        save_money()
    elif num == 3:
        get_money()
    elif num == 4:
        print("程序退出。")
        break
    else:
        print("没有这个选项，请重新输入")
        continue
