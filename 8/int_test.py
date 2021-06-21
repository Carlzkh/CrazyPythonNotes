"""
object.__str__(self) 对应于调用内置的str()函数将 亥对象转换成字符串。
object.__bytes__(self) 对应于调用内置的 bytes()函数将该对象转换 字节内容。该方法应该返回 byte对象。
object.__complex__(self) ：对应于调用内置的 complex()函数将该对象转换成复数。该方法应该返回complex对象
object.__int__(self) ：对应于调用内置的 int()函数将对象转换成整数。该方法应该返回 int对象
object.__float__(self) ：对应于调用内置的 float()函数将对象转换成浮点数 该方法应该返回float对象

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
    # 定义 nt 方法，程序可谓用 int （）函数将该对象转换成整数

    def __int__(self):
        return int(self.width * self.height)

    def __repr__(self):
        return 'Rectangle(width=%g height=%g)' % (self.width, self.height)


r = Rectangle(4, 5)
print(int(r))  # 20
