my_str = "itheima"

# 通过下标索引取值
value1 = my_str[2]
print(value1)

# index方法
value2 = my_str.index("h")
print(value2)

# replace方法  ——>字符串的替换
# 格式字符串.replace(被替换字符串，新字符串)
print(my_str)
new_my_sre = my_str.replace("it", "程序")
print(my_str)
print(new_my_sre)

print("------------分割字符串--------------")
# split方法   ——>分割字符串   split分割、分裂
# 格式：字符串.split(分割符字符串)
my_str = "python and Java"
print(my_str)
my_list = my_str.split(" ")
print(my_list)

print("------------去除字符串--------------")
# strip方法  （字符串的规整操作————>去除前后空格和换行符\n）  strip 去除
# 格式：字符串.strip()
# 格式：字符串.strip(字符串)
my_str1 = " python and Java "
print(my_str1)
new_my_sre = my_str1.strip()
print(new_my_sre)  # 去除了前后的空格或者换行符\n
print(type(new_my_sre))

print("------------华丽分割线--------------")
my_str2 = "12python and Java21"
print(my_str2)
new_my_sre2 = my_str2.strip("12")# 去除字符串”1“和字符串”2“
print(new_my_sre2)

print("------------华丽分割线--------------")
# 统计字符串某字符串的出现次数
print(my_str)
num = my_str.count("a")
print(f"my_str字符串中出现a的次数是：{num}")

# 统计字符串的长度
length = len(my_str)
print(f"my_str字符串中的长度是：{length}")




