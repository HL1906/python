# 规则1：内容限定，限定中文、英文、数字和下划线  注意：不能以数字开头
name_ = "zhangsan"
_name = "lisi"
name_1 = "wangwu"
张三 = "李四"
print(name_)
print(_name)
print(name_1)
print(张三)
print("--------------------------")

# 规则2：大小写敏感
Itheima = "黑马程序员"
itheima = 666
print(Itheima)
print(itheima)
print("--------------------------")

# 规则3：不能使用关键字
Class = 1.0
print(Class)
