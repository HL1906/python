"""
结合前面学习的input语句，完成如下案例
1.通过input语句，获取键盘输入，为变量age赋值。（注意转换成数字类型）
2.通过if判断是否成年，满足条件则输出提示信息“您已经成年，游玩需要补票10元”——>祝您游玩愉快
"""

# 获取键盘输入
age = input("请输入您的年龄：")
age = int(age)
if age >= 18:
    print("您已经成年，游玩需要补票10元。")
print("祝您游玩愉快！！!")
