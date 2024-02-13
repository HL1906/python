# 基本捕获语法
# try:
#     f = open("D:/abc.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常了，因为文件不存在。")
#     f = open("D:/abc.txt", "w", encoding="UTF-8")
import fileinput

# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了变量未定义的异常")

# 捕获多个异常
# try:
#     print(name)
#     1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除于零的异常错误")

# 未正确设置捕获异常类型，将无法捕获异常

# 捕获所以异常
try:
    print("hello")
    # f = open("D:/123.txt", "r")
    # print(name)
    # 1 / 0
except Exception as e:
    print("出现了异常")
else:
    print("好高兴，没有异常，这时候我可以执行")
finally:
    print("我是finally，有没有异常我都执行")

