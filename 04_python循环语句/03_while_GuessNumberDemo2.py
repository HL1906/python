import random
num = random.randint(1, 100)
# print(num)
count = 0
while True:
    guess_num = int(input("请输入你猜的数字"))
    count += 1
    if guess_num > num:
        print("大了")
    elif guess_num < num:
        print("小了")
    else:
        print("恭喜你猜中了")
        break
print("总共猜测了", count, "次")

