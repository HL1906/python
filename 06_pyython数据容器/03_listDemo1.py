# """
# 有一个列表，内容是：[21，25，21，23，22，20]
# 请通过列表的功能（方法），对其进行
# 1.定义这个列表，并且变量接受它
# 2.追加一个数字31，到列表的尾部
# 3.追加一个新列表[29，33，30]到列表的尾部
# 4.取出第一个元素（应是：21）
# 5.取出最后一个元素（应是：30）
# 6.查找元素31，在列表中的下标位置
# """

my_list = [21, 25, 21, 23, 22, 20]
my_list.append(31)
my_list.extend([29, 33, 30])
print(my_list)
first = my_list[0]
print(first)
end = my_list[-1]
print(end)
index = my_list.index(31)
print(index)
print(my_list)

