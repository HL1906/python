from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\python\python3.11.4/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("text_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd1 = sc.parallelize([1, 2, 3, 4, 5])


def func(data):
    return data * 10


rdd2 = rdd1.map(func)

print(rdd2.collect())

# 链式调用
rdd3 = rdd2.map(lambda x: x + 5).map(lambda x: x + 5)
