"""
+加   -减     *乘      /除
//取整除      %取余     **指数
=赋值运算符
+=加法赋值运算符    -=减法赋值运算符
*=乘法赋值运算符    /=除法赋值运算符
%=取模赋值运算符    **=幂赋值运算符
//=取整除赋值运算符
"""

print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)
print("11 // 2 = ", 11 // 2)
print("9 % 2 = ", 9 % 2 )
print("3 ** 2 = ", 3 ** 2)


print("-------------------")
num = 1
num += 1
print("num +=1:",num)

num -=1
print("num -=1:", num)

num *=4
print("num *=4:", num)

num /=2
print("num /=2:", num)

num = 3
num %=2
print("num %=2:", num)

num **=2
print("num **=2:", num)

num = 9
num //=2
print("num //=2:", num)