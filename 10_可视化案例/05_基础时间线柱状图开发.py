from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 35, 30], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()


bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [65, 80, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 构建时间线对象 和 # 主题设置
timeline = Timeline({"theme": ThemeType.LIGHT})
# 在时间线内添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 绘图是用时间线对象绘图，不是bar对象了
timeline.render("基础时间线柱状图.html")
