# 准备列表，列表内每一个元素都是字典，将其转换成为JSON
import json

data = [{"name": "张大山", "age": 11}, {"name": "赵小虎", "age": 11}]
json_str = json.dumps(data, ensure_ascii=False) # ensure_ascii=False如果要转成中文就要加这个
print(f"json_str格式是：{type(json_str)}")
print(f"json_str内容是：{json_str}")

# 准备字典，将字典转换成为JSON
data_2 = {"name": "周杰伦", "address": "台北"}
json_str = json.dumps(data_2, ensure_ascii=False)
print(f"json_str格式是：{type(json_str)}")
print(f"json_str内容是：{json_str}")

# 将JSON字符串转换成为python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "张大山", "age": 11}, {"name": "赵小虎", "age": 11}]'
l = json.loads(s)
print(f"l的格式是：{type(l)}")
print(f"l的内容是：{l}")

# 将JSON字符串转换成为python数据类型{k: v, k: v}
s = '{"name": "周杰伦", "address": "台北"}'
d = json.loads(s)
print(f"d的格式是：{type(d)}")
print(f"d的内容是：{d}")
