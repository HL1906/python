# 方法一：使用print直接输出类型信息
print(type(666))
print(type(13.14))
print(type("黑马程序员"))
print("--------------------------------------")

# 方法二：使用变量存储type()语句的结果
String_type = type("黑马程序员")
int_type = type(666)
float_type = type(13.14)
print(String_type)
print(int_type)
print(float_type)

print("--------------------------------------")
# 方法三：使用type()语句，查看变量中存储的数据类型信息
name = "黑马程序员"
name_type = type(name)
print(name_type)