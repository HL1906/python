"""
filter方法的作用是过滤数据
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python3.11.4/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("text_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# 对RDD的数据进行过滤
rdd2 = rdd.filter(lambda num: num % 2 ==0)
print(rdd2.collect())



