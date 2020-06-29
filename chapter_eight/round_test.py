"""
object.__format__(self, format_spec)：对应于调用内置的format()函数将对象转换成格式化字符串
object.__hash__(self)对应于调用内置的 hash()函数来获取该对象的 hash 码。
object.__abs__(self)：对应于调用内置的abs()函数返回绝对值
object.__round__(self[, ndigits])：对应于调用内置的 round （） 函数执行四舍五入取整。
object.__trunc__(self)：对应于调用内置的 trunc()函数执行截断取整
    如果某自定义类没有实现__int__(self)方法，而实现了__trunc__(self)方法，则该类对象调用int()函数时将执行__trunc__(self)
object.__floor__(self)：对应于调用内置的 floor()函数执行向下取整。
object.__ceil__(self)：对应于调用内置的 ceil()函数执行向上取整。
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义 setSize （）函数
    def setsize(self, size):
        self.width, self.height = size

    # 定义 getSize （）函数
    def getsize(self):
        return self.width, self.height
    # 使用 property 定义属性
    size = property(getsize, setsize)
    # 定义＿round一方法，程序可调用 round （）函数将该对象执行四舍五入取整

    def __round__(self, digits=0):
        self.width, self.height = round(self.width, digits), round(self.height, digits)
        return self

    def __repr__(self):
        return 'Rectangle(width=%g height=%g)' % (self.width, self.height)


r = Rectangle(4.13, 5.56)
# 对Rectangle对象执行四舍五入取整
result = round(r, 1)
print(r)  # Rectangle(width=4.1, height=5.6)
print(result)  # Rectangle(width=4.1, height=5.6)
