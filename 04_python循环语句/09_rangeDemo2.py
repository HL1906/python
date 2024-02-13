# 统计1-100(不包含100)中有多少个偶数
count = 0
for x in range(1, 100):
    if x % 2 == 0:
        print(x)
        count += 1
print(f"1-100中有{count}个偶数")
