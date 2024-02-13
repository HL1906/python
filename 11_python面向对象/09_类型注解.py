# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: str = "itheima"
var_3: bool = True


class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list1: list = [1, 2, 3]
my_tuple1: tuple = (1, "itheima", True)
my_dict1: dict = {"itheima": 666}

# 容器类型详细注解

my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[int, str, bool] = (1, "itheima", True)
my_dict2: dict[str, int] = {"itheima": 666}

# 在注释中进行注解
var1 = random.randint(1, 10)  # type: int
var2 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]


def func():
    return 10


var3 = func()  # type: int
