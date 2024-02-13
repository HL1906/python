if int(input("请输入你的身高：（cm）")) > 120 :
    print("你的身高大于120CM,不能免费游玩。")
    print("如果你的VIP等级大于3，可以免费游玩。")

    if int(input("请输入你的vip等级：（1-5）")) > 3:
        print("你的vip等级大于3，可以免费游玩。")
    else:
        print("对不起，你的vip等级不够，不能免费游玩。")

else:
    print("小朋友，你可以免费游玩哦！！！")