print("-----------------一-------------------")
# 通过占位的形式，完成拼接
name = "黑马程序员"
message = "学IT就来: %s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)


name = "传智播客"
set_up_year = 2006
stock_price = 19.99
message = "%s,成立于：%d，今天的股价是：%f" % (name, set_up_year, stock_price)
print(message)

print("-----------------二-------------------")

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1) # 空格空格空格11
print("数字11宽度限制1，结果是：%1d" % num1) # 11
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2) # 空格空格11.35
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2) # 11.35

print("-----------------三-------------------")

# 演示第二种字符串格式化方式：f"{占位}"
# f: format
print(f"我是{name}，我成立于：{set_up_year}年，我今天的股价是：{stock_price}")

print("-----------------四-------------------")
# 演示对表达式进行字符串的格式化
print("1 * 1 的结果是：%d" % (1 * 1))
print(f"1 * 2的结果是：{1 * 2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))