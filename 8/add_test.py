"""
object.__add__(self, other)：加法运算，为 “＋”运算符提供支持
object.__sub__（se f, other）：减法运算，为"-运算符提供支持。
object.__mul__（self, other）：乘法运算，为“＊”运算符提供支持。
object.__matmul__（self other）：矩阵乘法，为“＠”运算符提供支持
object.__truediv__（ If, other ：除法运算，为“／”运算符提供支持。
object.__floordiv__ (self, other ）： 整除运算 ，为“// ”运算符提供支持。
object.__mod__(self, other）：求余运算，为“%”运算符提供支持
object.__divmod__(self, other）：求余运算，为 divmod 算符提供支持。
object.__pow__（self other[, modulo］）：乘方运算，为“＊＊”运算符提供支持。
object.__lshift__（self, other）：左移运算，为“<<”运算符提供支持
object.__rshift__（self, other）： 右移运算，为“>>”运算符提供支持。
object.__and__（self, other）：按位与运算，为“＆”运算符提供支持。
object.__xor__(self, other) 按位异或运算，为“^”运算符提供支持。
object.__or__(self, other) ：按位或运算，为“｜”运算符提供支持。
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

    def __add__(self, other):
        # 要求参与“＋”运算的另一 操作数必须是 Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('＋运算要求目标是Rectangle')
        return Rectangle(self.width + other.width, self.height + other.height)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


rl = Rectangle(4, 5)
r2 = Rectangle(3, 4)
# 对两个 Rectangle 执行加法运算
r = rl + r2
print(r)  # Rectangle(width=7 , height=9)
