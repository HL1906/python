# 计算字符串有多少个字母a
name = "itheima is a barnd of itcast"

count = 0
for i in name:
    if i == "a":
        count += 1

print(f"被统计的字符串中有{count}个a")
