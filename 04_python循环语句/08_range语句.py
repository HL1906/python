# 演示range()语句的基本使用

# range语法1 range(num)

print("------------range语法1------------")

num = range(10) # 获取的就是[0-9]
for x in num:
    print(x, end='')    #
print()

print("------------------------range语法2---------")

# range语法二 range(num1, num2)
for x in range(5,10):# [5-9]
    print(x, end='') # [5-9]
print()

print("---------------------range语法3-------------")

#range语法3： range(num1,num2,step)
#从num1开始到num2结束，但不包含num2，step是间隔

for x in range(5, 10, 2):# [5,7,9]
    print(x, end='') # [5,7,9]

print()

i = 1
while i <=10:
    print(f"送第{i}朵玫瑰花")
    i += 1

for x in range(1, 11):
    print(f"送第{x}朵玫瑰花")
