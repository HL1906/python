class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")


# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # print("使用5g网络进行通话")
        # 方法1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方法2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

# 在子类调用父类成员
# 格式1：父类名.成员变量
#       父类名.成员方法(self)


# 格式2： super().成员变量
#        super().成员方法
