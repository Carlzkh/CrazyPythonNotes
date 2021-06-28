import matplotlib.pyplot as plt
import numpy as np

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

plt.bar(x=x_data, height=y_data, label='疯狂Java讲义', color='steelblue', alpha=0.8)
plt.bar(x=x_data, height=y_data2, label='疯狂Android讲义', color='indianred', alpha=0.8)

# 在柱状图上显示具体 数值， ha 参数控制水平对齐方式， va 参数控制垂直对齐方式
for x, y in enumerate(y_data):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt .text(x, y + 200, '%s' % y, ha='center', va='top')
# 设置标题
plt.title('Java与Android图书对比')
plt.xlabel('年份')
plt.ylabel('销量')

plt.legend()
plt.show()
