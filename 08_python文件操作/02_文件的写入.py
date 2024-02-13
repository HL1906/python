# 打开文件，不存在的文件

f = open("D:/python.txt", "w", encoding="UTF-8")

# write写入
f.write("hello world")  # 将内容写进内存中

# flush刷新
f.flush()               # 将内存中积攒的内容，写入到硬盘的文件中
# 关闭文件
f.close()               # close里面内置flush功能的

