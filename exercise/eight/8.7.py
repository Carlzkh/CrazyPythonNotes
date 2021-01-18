"""
7. 自定义 1个代表 2维坐标系上某个点的 Point 类（包括 两个属性），为 Point 类提供自
定义的减法运算符支持，计算结果返回两点之间的距离
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = other.x - self.x
        y = other.y - self.y
        return pow((pow(x, 2) + pow(y, 2)), 0.5)


point1 = Point(1, 2)
point2 = Point(2, 3)
print(point1 - point2)
