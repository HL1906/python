# 统计字符串的长度，并且不适应内置函数
str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是：{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度是：{count}")

print("-----------------函数-----------------------")


# 使用函数，来优化这个过程
def my_len(date):
    count1 = 0
    for j in date:
        count1 += 1
    print(f"字符串{date}的长度是：{count1}")


my_len(str1)
my_len(str2)
my_len(str3)
