i = float(input("请配合测量体温:"))


def check(i):
    if i <= 37.5:
        print("体温正常，可以进入")
    else:
        print(f"您当前的体温为{i}，高于37.5，请不要进入")


check(i)
