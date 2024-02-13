# number = int(input('请输入：'))
# for i in range(number) if number > 0 else range(number, 0):
#     if (i % 2 == 0):
#         pass
#     else:
#         print("奇数%s"%i)



# def jishu(number):
#     for i in range(number) if number > 0 else range(number, 0):
#         if (i % 2 == 0):
#             pass
#         else:
#             print("奇数%s"%i)
#
# number = int(input('请输入：'))
# jishu(number)


def club2(num):
    for i in range(num):
        if(i % 2 == 0):
            pass
        else:
            print("奇数为：%s"%i)

def club1(number):
    for i in range(number,0):
        if(i % 2 == 0):
            pass
        else:
            print("奇数为：%s"%i)

number = int(input('请输入：'))
if number > 0:
    club2(number)
else:
    club1(number)

