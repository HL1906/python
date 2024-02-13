"""
演示python的包
"""

# 创建一个包
# 导入自定义的包中的模块，并且使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过__all__变量，控制import *
from my_package import *
my_module1.info_print1()
# my_module2.info_print2()  # 使用不了，因为在_init_模块中控制了all变量
