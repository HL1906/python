# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]


def choose_sort_key(element):
    return element[1]


# 排序，基于带名函数
# my_list.sort(key=choose_sort_key, reverse=True)
# """
# reverse 反转：默认是从小到大，反转就是从发到小，所以填True
# """

# 排序基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)


print(my_list)
