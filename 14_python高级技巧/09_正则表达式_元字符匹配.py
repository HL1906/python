# 匹配账号，只允许字母和数字组成，长度6-10位
import re

# r = "^[a-zA-Z0-9]{6,10}$"
# s = "123456"
# print(re.findall(r, s))


# 匹配qq号，要求纯数字，长度5-10，第一位不能是0
# r = r"^[1-9]\d{4,9}$"
# s = "123456789"
# print(re.findall(r, s))


# 匹配邮箱地址，只允许qq、163、gmail这三个邮箱地址
r = r"^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$"
s = "25212@qq.com"
print(re.match(r, s))

