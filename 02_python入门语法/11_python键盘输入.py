# 演示python的input语句
# 获取键盘输入的信息

print("请告诉我你是谁：")
name = input()
print("我知道了，你是：%s" % name)

print("----------修改-----------")

# 修改
name = input("请输入你的名字：")
print(f"你的名字是：{name}")

print("----------数据类型转换-----------")

#输入数字类型
num = input("请告诉我你的银行卡密码：")
# 数据类型转换
num = int(num)
print("你的银行卡密码的类型是：", type(num))
