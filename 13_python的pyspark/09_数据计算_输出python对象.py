from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python3.11.4/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("text_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd_list: list = rdd.collect()
print(rdd_list)

# reduce算子，对RDD进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)

# take算子，取出RDD前N个元素，组成list返回
take_list = rdd.take(3)
print(take_list)

# count,换计RDD内有多少条数据，返回值为数字
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")

sc.stop()


