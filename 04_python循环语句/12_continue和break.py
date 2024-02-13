# continue
print("-------------continue-------------")
for i in range(1, 6):
    print("语句1")
    # continue 跳过本次循环
    continue
    print("语句2")
print()

print("-------------break-------------")
# break 结束本次循环

for i in range(1, 6):
    print("语句1")
    break
    print("语句2")
print("语句3")