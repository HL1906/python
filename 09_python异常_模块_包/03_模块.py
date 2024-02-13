# 使用import导入time模块的sleep功能
# import time     # 导入python内置的time模块
# print("你好")
# time.sleep(2)
# print("我好")

# 使用form导入time的sleep功能
# from time import sleep
# print("你好")
# sleep(2)
# print("我好")


# 使用 * 导入time模块的全部功能
# from time import *
# print("你好")
# sleep(2)
# print("我好")

# 使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(2)
# print("我好")

from time import sleep as sl
print("你好")
sl(2)
print("我好")
