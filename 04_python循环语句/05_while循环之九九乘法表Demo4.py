# 九九乘法表

# 定义外层循环
i = 1
while i <= 9:

    # 定义 内层循环
    j = 1
    while j <= i:
        result = i * j
        # 内循环的print语句，不换行，通过\t制表符进行对齐
        print(f"{j} * {i} = {result}\t", end='')
        j += 1

    i += 1
    print()

