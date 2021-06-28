import matplotlib.pyplot as plt
from matplotlib import font_manager
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
y_data3 = [50200, 58220, 51520, 52320, 57820, 59720, 62820]
# 中文字体路径（先看好自己电脑中的路径），legend(prop=font)就可以使用对应语言了
font = font_manager.FontProperties(fname='C:/Windows/fonts/SIMLI.TTF')

ln1 = plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
ln2 = plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.')
ln3 = plt.plot(x_data, y_data3, color='pink', linewidth=4.0, linestyle='-.')
# 下面legend()函数的handles参数可以不传，默认按参数定义顺序
# plt.legend(handles=[ln2, ln1], labels=['疯狂Android讲义年销量', '疯狂Java讲义年销量'], prop=font, loc='best')
plt.legend(labels=['疯狂Android讲义年销量', '疯狂Java讲义年销量'], prop=font, loc='best')
plt.show()
