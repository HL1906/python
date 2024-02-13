# 私有成员，在前面加__
class Phone:
    __name = None
    __price = None

    def __cal(self):
        print("正在打电话")

    def __init__(self, name, price):
        self.__name = name
        self.price = price
        print(f"手机信息为：name:{self.__name}, price:{self.price}")
        self.__cal()


p1 = Phone("小米", 2399)
