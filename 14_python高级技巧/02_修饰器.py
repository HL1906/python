# 装饰器一般写法（闭包）
# def outer(func):
#     def inter():
#         print("我睡觉啦")
#         func()
#         print("我起床啦")
#
#     return inter
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中......")
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn()

# 装饰器的快捷写法（语法糖）
def outer(func):
    def inter():
        print("我睡觉啦")
        func()
        print("我起床啦")

    return inter


@outer
def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))


sleep()
