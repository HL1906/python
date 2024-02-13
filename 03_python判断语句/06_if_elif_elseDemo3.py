# 定义键盘输入获取身高数据
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的vip等级（1-5）："))



# 通过if判断,可以使用多条件判断的语法
# 第一个条件就是if
if height <= 120:
    print("您的身高小于120cm，可以免费游玩。")
elif vip_level > 3:
    print("vip等级大于3，可以免费游玩。")

# 也可以像下方这样写
elif int(input("请输入今天的日期：")) == 1:
    print("今天是1号，可以免费游玩。")
else:
    print("不好意思，条件不满足，需要买票，10元。")

print("祝您游玩愉快！！！")
