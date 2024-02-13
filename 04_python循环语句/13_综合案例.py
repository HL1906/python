# """
# 某公司，账户余额有1W元，给20名员工发工资。
# 1.员工标号从1-20，从编号1开始，依次领取工资，每人可领取1000元
# 2.领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5分，不发工资，换下一位
# 3.如果工资发完了，结束发工资
# """
money = 10000
for i in range(1,21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效分{score}，不满足，不发工资，下一位")
        continue

    if money >=1000:
        money -= 1000
        print(f"员工{i}，满足条件发工资1000元，公司账户余额剩余：{money}元")
    else:
        print(f"余额不足，当前余额为：{money}元，结束发工资")
        break