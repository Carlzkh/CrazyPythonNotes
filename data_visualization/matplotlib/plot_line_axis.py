import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

ln1 = plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--', label='疯狂JAva讲义')
ln2 = plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.', label='疯狂Android讲义')

plt.legend(loc='upper left')

plt.xlabel("年份")
plt.ylabel("图书销量（本）")
plt.title('疯狂图书历年销量')

plt.yticks([50000, 70000, 100000], ['挺好', '优秀', '火爆'])

ax = plt.gca()
# 设置x轴的刻度值放在底部x轴上
ax.xaxis.set_ticks_position('bottom')
# 设置y轴的刻度值放在左边y轴上
ax.yaxis.set_ticks_position('left')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('red')
# 定义底部坐标线的位置
ax.spines['bottom'].set_position(('data', 70000))
plt.show()
