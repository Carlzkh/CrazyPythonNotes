"""
object.__iadd__(self, other)：加法运算，为 “＋=”运算符提供支持
object.__isub__（se f, other）：减法运算，为"-=运算符提供支持。
object.__imul__（self, other）：乘法运算，为“＊=”运算符提供支持。
object.__imatmul__（self other）：矩阵乘法，为“＠=”运算符提供支持
object.__itruediv__（ If, other ：除法运算，为“／=”运算符提供支持。
object.__ifloordiv__ (self, other ）： 整除运算 ，为“//=”运算符提供支持。
object.__imod__(self, other）：求余运算，为“%=”运算符提供支持
object.__idivmod__(self, other）：求余运算，为 divmod= 算符提供支持。
object.__ipow__（self other[, modulo］）：乘方运算，为“＊＊=”运算符提供支持。
object.__ilshift__（self, other）：左移运算，为“<<=”运算符提供支持
object.__irshift__（self, other）： 右移运算，为“>>=”运算符提供支持。
object.__iand__（self, other）：按位与运算，为“＆=”运算符提供支持。
object.__ixor__(self, other) 按位异或运算，为“^=”运算符提供支持。
object.__ior__(self, other) ：按位或运算，为“｜=”运算符提供支持。
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义 setSize （）函数
    def set_size(self, size):
        self.width, self.height = size

    # 定义 getSize()函数
    def get_size(self):
        return self.width, self.height
    # 使用 property 定义属性
    size = property(get_size, set_size)
    # 定义__add__方法，该对象可执行“＋”运算

    def __iadd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('＋=运算要求目标是数值')
        return Rectangle(self.width + other, self.height + other)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r1 += 3
print(r1)  # Rectangle(width=7 , height=9)
