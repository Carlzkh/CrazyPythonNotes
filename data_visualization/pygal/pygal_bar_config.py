import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

bar = pygal.Bar()
bar.add('疯狂Java讲义', y_data)
bar.add('疯狂Android讲义', y_data2)
bar.x_labels = x_data
bar.title = '疯狂图书的历年销量'
bar._x_title = '年份'
bar._y_title = '销量'

# 设置 轴的刻度值旋转 45
bar.x_label_rotation = 45
# 设置将图例放在底部
bar.legend_at_bottom = True
# 设置数据图四周的页边距
# 也可通过 rnargin_bottorn rnargi 口＿left rnargi 口＿ right margin top 只设置单独一边的页边距
bar.margin = 35
# 隐藏 轴上的网格线
bar.show_y_guides = False
# 显示 轴上的网格线
bar.show_x_guides = True 
# 指定将数据图输出 SVG 文件中
bar.render_to_file('fk_books_config.svg')
