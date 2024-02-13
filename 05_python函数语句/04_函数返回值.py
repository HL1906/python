def add(x, y):
    result = x + y
    return result


r = add(5, 5)
print(r)
print(add(6, 6))

print("----------------None----------------------")


def say_hi():
    print("你好呀！")


result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")
