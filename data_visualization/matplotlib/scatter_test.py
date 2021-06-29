import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)
plt.scatter(x_data, np.sin(x_data), c='purple',  # 设置点的颜色
            s=50,  # 设置点的半径
            alpha=0.5,  # 设置点的半径
            marker='p',  # 设置使用五边形标记
            linewidths=1,  # 设置边框的线宽
            edgecolors=['green', 'yellow'])  # 设置边框的颜色

plt.scatter(x_data[0], np.sin(x_data)[0], c='red', s=150, alpha=1)
plt.scatter(x_data[63], np.sin(x_data)[63], c='black', s=150, alpha=1)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线的散点图')
plt.show()
