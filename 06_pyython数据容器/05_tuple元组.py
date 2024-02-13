"""
演示tuple元组的定义和操作
"""

# 定义元组
t1 = ("hello", 1, True)
# 获取空的元组
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元组
t4 = ("hello") # 这个是字符串，还要在后面加上一个单独的逗号
print(f"t4的类型是：{type(t4)},内容是：{t4}")
t5 = ("hello",)
print(f"t5的类型是：{type(t5)},内容是：{t5}")
# 元组的嵌套
t6 = ((1, 2, 3), (4, 5, 6))
print(f"t6的类型是：{type(t6)},内容是：{t6}")

# 下标索引取取出内容
print(t6[1][2])

# 元组的操作：index查找方法
t7 = ("张三", "李四", "王五")
index = t7.index("张三")
print(f"在元组t7中查找张三的索引是：{index}")

# 元组的操作：count统计元组元素数量
t8 = ("张三", "李四", "张三", "张三", "王五")
num = t8.count("张三")
print(f"在t8元组中，统计张三的数量{num}")

# 元组操作：len函数统计元组元素的数量
length = len(t8)
print(length)

# 元组的遍历：while
index = 0
while index < len(t7):
    print(f"元组的元素有：{t7[index]}")
    index += 1

# 元组的遍历：for
for element in t7:
    print(f"2元组的元素有：{element}")



"""
元组本身是不能修改的，
但是如果元组里面存储的是列表，对列表进行修改
"""
Tuple = (1, 2, 3, [4, 5, 6])
print(f"Tuple元组的内容是：{Tuple}")
Tuple[3][0] = 7
Tuple[3][1] = 8
Tuple[3][2] = 9
print(f"Tuple元组修改后的内容是：{Tuple}")




