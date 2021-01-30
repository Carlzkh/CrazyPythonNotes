"""
3. 定义代表二维坐标系上某个点的 Point 类（包括 x,y两个属性），为该类提供 个方法用
于计算两个 Point 之间 的距离 再提供一个方法用于判断 Point 组成的三角形是 、锐角还
是直角三角形
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point1):
        x = point1.x - self.x
        y = point1.y - self.y
        return pow(pow(x, 2) + pow(y, 2), 0.5)

    def triangles_type(self, point1, point2):
        a = self.distance(point1)
        b = point1.distance(point2)
        c = point2.distance(self)
        # print('初始abc', a, b, c)

        if a >= b:
            a, b = b, a
            if b > c:
                b, c = c, b
        else:
            if b > c:
                b, c = c, b
        # print('排序abc：', a, b, c)

        if a + b == c:
            print('三点共线，不是三角形！')
        else:
            if a * a + b * b > c * c:
                print('此三角形是锐角三角形！')
            elif a * a + b * b == c * c:
                print('此三角形是直角三角形！')
            else:
                print('此三角形是钝角三角形！')


point_a = Point(0, 1)
point_b = Point(1, 2)
point_c = Point(4, 3)
print(point_a.distance(point_b))
point_a.triangles_type(point_b, point_c)
point_b.triangles_type(point_a, point_c)
point_c.triangles_type(point_a, point_b)
point_a.triangles_type(point_c, point_b)
point_b.triangles_type(point_c, point_a)
point_c.triangles_type(point_b, point_a)
point_c.triangles_type(point_b, point_b)
