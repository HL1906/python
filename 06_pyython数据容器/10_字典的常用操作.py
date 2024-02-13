# 字典新增元素
my_dict = {"张三": 99, "李四": 88, "王五": 77}

# 新增元素
my_dict["赵六"] = 66
print(f"字典经过新增元素后的结果:{my_dict}")

# 更新元素
my_dict["赵六"] = 88
print(f"字典经过更新元素后的结果:{my_dict}")

# 删除元素
score = my_dict.pop("张三")
print(f"字典中被移除了一个元素，结果是：{my_dict}，张三的考试分数是：{score}")
# 清空字典
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

# 获取全部key的方法
# 格式：字典.keys()
my_dict = {"张三": 99, "李四": 88, "王五": 77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")


# 字典遍历
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

print("---------------华丽分割线-------------------------")
# 方式2：直接对字典进行for循环，每一次都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计字典内的元素
length = len(my_dict)
print(length)



