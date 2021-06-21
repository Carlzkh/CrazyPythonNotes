"""
object.__neg__(self) ：为单目求负（－）运算符提供支持
object.__pos__(self) 为单目求正（＋〉运算符提供支持
object.__invert__(self) 为单目取反（ 〉运算符提供支持
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义 setSize （）函数
    def set_size(self, size):
        self.width, self.height = size

    # 定义 getSize （）函数
    def get_size(self):
        return self.width, self.height
    # 使用 property 定义属性
    size = property(get_size, set_size)
    # 定义 neg 方法，该对象可执行求负（ ）运算

    def __neg__(self):
        self.width, self.height = self.height, self.width

    def __repr__(self):
        return 'Rectangle(width=%g height=%g)' % (self.width, self.height)


r = Rectangle(5, 4)
# 对 Rectangle 执行求负运算
q = -r
print(r)  # Rectangle width=S height=4)
