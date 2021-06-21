"""
object.__lt__(self, other)：为“<”运算符提供支持。
object.__le__(self, other)：为“<=”运算符提供支持
object.__eq__(self, other)：为“==”运算符提供支持
object.__ne__(self, other)：为“!=”运算符提供支持。
object.__gt__(self, other)：为“>”运算符提供支持
object.__ge__(self, other)：为“>=”运算构提供支持
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 定义 sets ze （）函数

    def set_size(self, size):
        self.width, self.height = size
    # 定义 getSize （）函数

    def get_size(self):
        return self.width, self.height
    # 使用 property 定义属性
    size = property(get_size, set_size)
    # 定义＿gt 方法，该对象可支持“>”和"<”比较

    def __gt__(self, other):
        # 要求参与“〉”比较的另 个操作数必须是 Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('比较要求目标是Rectangle')
        return True if self.width * self.height > other.width * other.height else False
    # 定义＿eq一方法，该对象可支持“＝＝”和“！＝”比较

    def __eq__(self, other):
        # 要求参与“＝＝”比较的另一个操作数必须是 Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('＝＝比较要求目标是Rectangle')
        return True if self.width * self.height == other.width * other.height else False
    # 定义 ge 方法，该对象i:iJ 支持 〉＝”和“〈＝”比较

    def __ge__(self, other):
        # 要求参与“〉＝”比较的另一个操作数必须是 Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>=比较要求目标是Rectangle')
        return True if self.width * self.height >= other.width * other.height else False

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
print(r1 > r2)  # True
print(r1 >= r2)  # True
print(r1 < r2)  # False
print(r1 <= r2)  # False
print(r1 == r2)  # False
print(r1 != r2)  # True
print("－－一－－－－－－－－－－－－－－－")
r3 = Rectangle(2, 6)
print(r2 >= r3)  # True
print(r2 > r3)  # False
print(r2 <= r3)  # True
print(r2 < r3)  # False
print(r2 == r3)  # True
print(r2 != r3)  # False
