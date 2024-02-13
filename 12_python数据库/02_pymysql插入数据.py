from pymysql import  Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名（IP）
    port=3306,          # 端口
    user="root",         # 账户
    password="123456",   # 密码
    autocommit = True    # 自动提交（确认）
)

cursor = conn.cursor()       # 获取到游标对象
# 选择数据库
conn.select_db("abcdb")

cursor.execute("insert into test_pymysql values(10002)")
# conn.commit()  # 要通过commit进行确认才能传入数据
conn.close()

