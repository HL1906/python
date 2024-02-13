"""
演示函数的多返回值
"""


def test_return():
    return 1, 2, 3


x, y, z = test_return()
print(x)
print(y)
print(z)
