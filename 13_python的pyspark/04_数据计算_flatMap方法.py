from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python3.11.4/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("text_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["itheima, itcast, 666", "ieheima, itheima, python", "python, zhangsan"])

# flatMap功能可以解除嵌套
rdd2 = rdd.flatMap(lambda x: x.splist(" "))
print(rdd2.collect())

