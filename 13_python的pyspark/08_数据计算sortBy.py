from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python3.11.4/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("text_spark")
sc = SparkContext(conf=conf)

# 1.读取数据文件
rdd = sc.textFile("D:/hello.text")
# 2.取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 3.将所有单词都转换成二元元组，单词成为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 4.分组并且求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a +b)
# 对结果进行排序
final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(final_rdd.collect())

