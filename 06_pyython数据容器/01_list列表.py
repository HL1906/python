"""
演示数据容器之list列表
语法：[元素1，元素2，...]
"""
# 定义一个列表list
my_list = ["itheima", "itcast", "python"]
print(list)
print(my_list)
print(type(my_list))
print("--------------------")
my_list = ["python", 666, True]
print(my_list)
print(type(my_list))
print("-----------取出列表-----------")
print(my_list[0])
print(my_list[1])
print(my_list[2])
print("---------华丽分割线----------")
# 如果是倒序则是 -1、-2、-3
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

print("-----------嵌套列表-----------")
# 定义一个嵌套列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))

print("-----------遍历嵌套列表-----------")
# 通过下标索引取出数据（倒序取出）
my_list = [["zhangsan", "lisi", "wangwu"], ["张三", "李四", "王五"], [1, 2, 3]]
print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])
print(my_list[1][0])
print(my_list[1][1])
print(my_list[1][2])
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# 取出嵌套列表的元素


