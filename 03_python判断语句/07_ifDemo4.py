# 定义一个变量
num = 5

if int(input("请输入一个数字")) == num :
    print("恭喜你，第一次就猜对了！")
elif int(input("猜错了，再猜一次。")) == num :
    print("不错喔，你猜对啦！！！")
elif int(input("猜错了，最后猜一次。")) == num :
    print("恭喜你，你猜对啦")
else:
    print("sorry,猜错了。")