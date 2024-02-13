my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}


# len元素个数
print(f"列表元素个数有：{len(my_list)}")
print(f"元组元素个数有：{len(my_tuple)}")
print(f"字符串元素个数有：{len(my_str)}")
print(f"集合元素个数有：{len(my_set)}")
print(f"字典元素个数有：{len(my_dict)}")

print("--------------------最大元素---------------------")
# max最大元素
print(f"列表最大的元素是：{max(my_list)}")
print(f"元组最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}")
print(f"集合最大的元素是：{max(my_set)}")
print(f"字典最大的元素是：{max(my_dict)}")

print("--------------------最小元素---------------------")
# min最小元素
print(f"列表最小的元素是：{min(my_list)}")
print(f"元组最小的元素是：{min(my_tuple)}")
print(f"字符串小的元素是：{min(my_str)}")
print(f"集合最小的元素是：{min(my_set)}")
print(f"字典最小的元素是：{min(my_dict)}")

print("--------------------类型转换：容器转列表---------------------")
# 类型转换：容器转列表
print(f"列表容器转列表的结果是：{list(my_list)}")
print(f"元组容器转列表的结果是：{list(my_tuple)}")
print(f"字符串容器转列表的结果是：{list(my_str)}")
print(f"集合容器转列表的结果是：{list(my_set)}")
print(f"字典容器转列表的结果是：{list(my_dict)}")

print("--------------------类型转换：列表转元组---------------------")
# 类型转换：容器转元组
print(f"列表容器转元组的结果是：{tuple(my_list)}")
print(f"元组容器转元组的结果是：{tuple(my_tuple)}")
print(f"字符串容器转元组的结果是：{tuple(my_str)}")
print(f"集合容器转元组的结果是：{tuple(my_set)}")
print(f"字典容器转列表的结果是：{tuple(my_dict)}")

print("--------------------类型转换：列表转字符串---------------------")
# 类型转换：容器转字符串
print(f"列表容器转字符串的结果是：{str(my_list)}")
print(f"元组容器转字符串的结果是：{str(my_tuple)}")
print(f"字符串容器转字符串的结果是：{str(my_str)}")
print(f"集合容器转字符串的结果是：{str(my_set)}")
print(f"字典容器转列表的结果是：{str(my_dict)}")

print("--------------------类型转换：列表转集合---------------------")
# 类型转换：容器转集合
print(f"列表容器转集合的结果是：{set(my_list)}")
print(f"元组容器转集合的结果是：{set(my_tuple)}")
print(f"字符串容器转集合的结果是：{set(my_str)}")
print(f"集合容器转集合的结果是：{set(my_set)}")
print(f"字典容器转列表的结果是：{set(my_dict)}")

print("--------------------sorted排序---------------------")
# sorted排序
# 升序：sorted(容器)
# 格式： sorted(容器,[reverse=True]) 降序
my_list = [3, 1, 2, 5, 4]
my_tuple = (5, 2, 3, 4, 1)
my_str = "bcadfeg"
my_set = {2, 3, 4, 1, 5}
my_dict = {"key4": 4, "key5": 5, "key3": 3, "key1": 1, "key2": 2}

print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

print("--------------------sorted降序排序---------------------")
# 降序排序    sorted-> 排序            reverse->相反的
print(f"列表对象的反向排序结果：{sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse=True)}")
