"""
3. 定义代表二维坐标系上某个点的 Point 类（包括 两个属性），为该类提供 个方法用
于计算两个 Point 之间 的距离 再提供一个方法用于判断 Point 组成的三角形是 、锐角还
是直角三角形
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance_point(point_a, point_b):
        return pow((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2, 0.5)

    @staticmethod
    def classify_triangles_by_sides(side_a, side_b, side_c):
        if side_a < (side_b + side_c):
            if side_a ** 2 == side_b ** 2 + side_c ** 2:
                print('abc三点组成直角三角形')
            elif side_a ** 2 < side_b ** 2 + side_c ** 2:
                print('abc三点组成锐角三角形')
            else:
                print('abc三点组成钝角三角形')
        else:
            print('abc三点不组成三角形，既abc在一条直线上')

    def classify_triangles_by_angles(self, a, b, c):
        ab = self.distance_point(a, b)
        bc = self.distance_point(b, c)
        ac = self.distance_point(a, c)
        print(ab, bc, ac)
        # max_side = max(ab, bc, ac)
        if ab >= bc:
            if (ab >= ac) & (ab < (ac + bc)):
                if ab * ab == ac * ac + bc * bc:
                    print('abc三点组成直角三角形')
                elif ab * ab < ac * ac + bc * bc:
                    print('abc三点组成锐角三角形')
                else:
                    print('abc三点组成钝角三角形')
            elif (ab < ac) & (ac < (ab + bc)):
                if ac * ac == ab * ab + bc * bc:
                    print('abc三点组成直角三角形')
                elif ac * ac < ab * ab + bc * bc:
                    print('abc三点组成锐角三角形')
                else:
                    print('abc三点组成钝角三角形')
            else:
                print('abc三点不组成三角形，既abc在一条直线上')
        else:
            if (bc >= ac) & (bc < (ac + ab)):
                if bc * bc == ac * ac + ab * ab:
                    print('abc三点组成直角三角形')
                elif bc * bc < ac * ac + ab * ab:
                    print('abc三点组成锐角三角形')
                else:
                    print('abc三点组成钝角三角形')
            elif (bc < ac) & (ac < (bc + ab)):
                if ac * ac == ab * ab + bc * bc:
                    print('abc三点组成直角三角形')
                elif ac * ac < ab * ab + bc * bc:
                    print('abc三点组成锐角三角形')
                else:
                    print('abc三点组成钝角三角形')
            else:
                print('abc三点不组成三角形，既abc在一条直线上')

    def classify_triangles_by_angles_2(self, point_a, point_b, point_c):
        ab = self.distance_point(point_a, point_b)
        bc = self.distance_point(point_b, point_c)
        ac = self.distance_point(point_a, point_c)
        print(ab, bc, ac)
        max_side = max(ab, bc, ac)
        if max_side == ab:
            self.classify_triangles_by_sides(ab, bc, ac)
        elif max_side == bc:
            self.classify_triangles_by_sides(bc, ab, ac)
        else:
            self.classify_triangles_by_sides(ac, bc, ab)


a = Point(1, 2)
b = Point(4, 4)
c = Point(3, 5)
a.classify_triangles_by_angles(a, b, c)
# print(a.distance_point(a, b))
a.classify_triangles_by_angles_2(a, b, c)
