# 打开文件
import time

f = open("D:/test.txt", "r", encoding="UTF-8")
print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果是：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")
print("-------------------------------------------")
# 读取文件 - readLines()
# lines = f.readlines()  # 读取文件的全部内容，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 —— readline() 一次读取一行
"""
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
line5 = f.readline()
print(f"第一行的内容是：{line1}")
print(f"第二行的内容是：{line2}")
print(f"第三行的内容是：{line3}")
print(f"第四行的内容是：{line4}")
print(f"第五行的内容是：{line5}")
"""

# for循环读取文件行
# for line in f:
#     print(f"每一行的内容是：{line}")

# 文件的关闭 close()
# time.sleep(50000000) # 程序持续睡眠的时间
# f.close()

# with open 语法操作文件
# 自动帮你关闭文件
# 格式：with open(...) as f:
with open("D:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的内容是：{line}")
