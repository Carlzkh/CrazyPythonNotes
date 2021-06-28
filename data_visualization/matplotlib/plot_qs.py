import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
plt.plot(x_data, y_data)
plt.show()

plt.plot(y_data)  # 自动使用0、1、2、3作为X轴数据
plt.show()
