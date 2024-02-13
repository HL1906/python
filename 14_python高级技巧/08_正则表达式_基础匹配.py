import re

s = "1python itheima python"

# match 从头匹配
result1 = re.match("python", s)
print(result1)
# print(result.span())
# print(result.group())

# search 搜索匹配
result2 = re.search("python", s)
print(result2)
# findall  搜索全部匹配
result3 = re.findall("python", s)
print(result3)


