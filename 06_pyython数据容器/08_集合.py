"""
演示数据容器集合的使用
"""
print("--------------定义集合------------------")
# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育"}
my_set_empty = set()  # 定义空集合
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

print("--------------添加新元素------------------")
# 添加新元素
my_set.add("python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")

print("--------------移除元素------------------")
# 移除元素
my_set.remove("itheima")
print(f"my_set移除后的结果是：{my_set}")


print("--------------随机取出一个元素------------------")
# 随机取出一个元素
print(my_set)
element = my_set.pop()
print(f"随机取出的元素是：{element}")
print(my_set)

print("--------------清空集合------------------")
# 清空集合
print(my_set)
my_set.clear()
print(f"清空集合的结果是：{my_set}")

print("--------------出2个集合的差集------------------")
# 取出2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 4, 6}
set3 = set1.difference(set2)
print(f"集合1原有的内容：{set1}")
print(f"集合2原有的内容：{set2}")
print(f"集合1和2的差集的内容：{set3}") # 集合1有而2没有的元素

print("--------------消除2个集合的差集------------------")
# 消除2个集合的差集
# 格式：集合1.difference_update(集合2)
# 功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果：集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除差集后集合1的结果{set1}")
print(f"消除差集后集合2的结果{set2}")

print("--------------2个集合合并为一个集合------------------")
# 2个集合合并为一个集合
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set4 = set1.union(set2)
print(f"集合1原有的内容：{set1}")
print(f"集合2原有的内容：{set2}")
print(f"合并后的集合结果是：{set4}")

print("--------------统计集合元素数量------------------")
# 统计集合元素数量
set5 = {1, 2, 3, 4, 5}
num = len(set5)
print(f"集合的个数：{num}")

print("--------------集合的遍历------------------")
# 集合的遍历
# 只能是for循环(因为set没有索引)
for element in set5:
    print(f"集合的元素有{element}")


