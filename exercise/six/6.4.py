"""
4. 定义代表三维笛卡尔坐标系上某 个点的 Point 类（包括 x，y，z三个属性），为该类定义一
个方法，可接收b，c，d三 个参数，用于计算当前点、b，c 组成的面与 b，c，d组成的面之间的
夹角。提示 cos 夹角 = (X.Y) ／|X||Y|， 其中 X=AB✖ BC, Y=BC× CD, X 的点积， AB✖BC
代表 AB BC 的叉乘
"""
import numpy


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def vector_quantity(self, point1):
        x = point1.x - self.x
        y = point1.y - self.y
        z = point1.z - self.z
        return x, y, z

    def plane_included_angle(self, b, c, d):
        ab = self.vector_quantity(b)
        bc = b.vector_quantity(c)
        cd = c.vector_quantity(d)
        x = numpy.cross(ab, bc)
        y = numpy.cross(bc, cd)
        return numpy.dot(x, y)/(abs(numpy.linalg.norm(x))*abs(numpy.linalg.norm(y)))


point_a = Point(1, 2, 3)
point_b = Point(2, 1, 2)
point_c = Point(3, 4, 1)
point_d = Point(4, 2, 3)
print(point_a.plane_included_angle(point_b, point_c, point_d))
