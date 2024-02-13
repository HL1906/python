"""
distinct方法是作用对数据去重
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python3.11.4/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("text_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 5, 6, 1, 3, 2, 7, 1, 5, ])

rdd2 = rdd.distinct()

print(rdd2.collect())
