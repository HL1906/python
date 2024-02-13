# 导入自定义模块

# from  my_module1 import testA
#
# testA(1, 2)


# 通过__all__变量，控制import *
from my_module1 import *
testA(1, 2)
# testB(2, 1) # 不能使用testB，因为定义了all

