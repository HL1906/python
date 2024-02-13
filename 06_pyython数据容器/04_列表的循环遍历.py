# 通过while循环遍历数组

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return None
    """
    my_list = [1, 2, 3, 4, 5]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引+1
    # 循环条件索引变量 < 列表的元素数量
    # 定义一个变量用来记录列表的下标
    index = 0  # 初始化元素数量
    while index < len(my_list): # while是一个值
        result = my_list[index]
        print(result)
        index += 1


def list_for_func():
    """
        :return:None
        """
    my_list = [1, 2, 3, 4, 5]
    index1 = 0
    for index1 in range(len(my_list)):# for是要一个范围
        element = my_list[index1]
        print(element)
        index1 += 1


list_while_func()
print("---------------华丽分割线-----------------")
list_for_func()


print("---------------for循环遍历-----------------")

# 第二种for循环遍历
my_list = ["zhangsan", "lisi", "wangwu"]
for element in my_list:
    print(f"列表的元素有：{element}")


