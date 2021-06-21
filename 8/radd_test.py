"""
object.__radd__(self, other)：当y提供该方法时，可执行 x + y
object.__rsub__（se f, other）：当y提供该方法时，可执行 x - y
object.__rmul__（self, other）：当y提供该方法时，可执行 x * y
object.__rmatmul__（self other）：当y提供该方法时，可执行 x @ y
object.__rtruediv__（ If, other ：当y提供该方法时，可执行 x / y
object.__rfloordiv__ (self, other ）： 当y提供该方法时，可执行 x // y
object.__rmod__(self, other）：当y提供该方法时，可执行 x % y
object.__rdivmod__(self, other）：当y提供该方法时，可执行 x divmod y
object.__rpow__（self other[, modulo］）：当y提供该方法时，可执行 x ** y
object.__rlshift__（self, other）：当y提供该方法时，可执行 x < y
object.__rrshift__（self, other）： 当y提供该方法时，可执行 x > y
object.__rand__（self, other）：当y提供该方法时，可执行 x & y
object.__rxor__(self, other) 当y提供该方法时，可执行 x ^ y
object.__ror__(self, other) ：当y提供该方法时，可执行 x | y
简单来说，定义类提供了上面列 rxxx()方法，那么该自定义类的对象就可以出现在对应运算符的右边
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

    def __radd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('＋运算要求目标是数值')
        return Rectangle(self.width + other, self.height + other)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r = 4 + r1
print(r)  # Rectangle(width=7 , height=9)
