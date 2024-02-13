# 定义列表对象
my_list = ["张三", "李四", "王五", "李四"]

# 1查找某元素在列表内的下标索引
print("--------查找某元素在列表内的下标索引--------")
index = my_list.index("张三")
print(f"张三在列表中的下标索引是：{index}")

print("--------修改特定下标索引--------")
# 2.修改特定下标索引
print(my_list[0])
my_list[0] = "zhangsan"
print(my_list[0])

print("--------插入元素--------")
# 3.在指定下标位置插入元素
# 格式： 列表名.insert(下标, 元素)
print(my_list)
my_list.insert(1, "赵六")
print(my_list)

print("--------添加一个元素--------")
# 4.在列表的尾部追加'''单个'''新元素
# 格式： 列表名.append()
print(my_list)
my_list.append("孙七")
print(my_list)

print("--------追加一批元素--------")
# 5.在列表尾部追加  一批  新元素
# 格式: 列表名.extend(其他数据容器)
print(my_list)
my_list.extend([4, 5, 6])
print(my_list)

print("-----------华丽分割线-----------")
my_list1 = [1, 2, 3]
print(my_list1)
my_list2 = [4, 5, 6]
my_list1.extend(my_list2)
print(my_list1)

print("-----------删除元素-----------")
# 6.删除指定下标索引元素（2种方法）
# 格式1：del 列表名[下标]
print(my_list)
del my_list[0]
print(my_list)
print("删除元素方法2")
# 格式2：列表名.pop(下标)
print(my_list)
element = my_list.pop(0)
print(f"通过pop删除的元素是：{element}")
print(my_list)

print("-----------删除某元素在列表中的第一个匹配项-----------")
# 删除某元素在列表中的第一个匹配项
# 格式：列表名.remove
my_list3 = ["1", "1", "2", "3", "3", "3", "3", "1", "4", ]
my_list3.remove("3") # 只能删掉一个元素
print(my_list3)

print("----------------清空列表--------------")
# 清空列表
# 格式：列表名.clear
print(my_list3)
my_list3.clear()
print(my_list3)

print("----------------统计列表内某元素的数量--------------")
# 9.统计列表内某元素的数量
# 格式：列表名.count(元素)
print(my_list)
count = my_list.count("李四")
print(f"列表中李四的数量是：{count}个")

print("----------------统计列表内全部元素的数量--------------")
# 10.统计列表全部的元素数量
# 格式：len(列表名)
print(my_list)
count = len(my_list)
print(f"列表全部元素的数量是：{count}个")

