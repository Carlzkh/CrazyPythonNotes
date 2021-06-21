"""
该对象具有的状态信息。
object 类提供的一repr一（）方法总是返回 该对象实现类的“类名＋ object at ＋内存地址”值，这
个返回值并不能真正实现“自我描述”的功能，因此，如果用户需要自定义类能实现“自我描述”
的功能，就必须重写一repr一（）方法。例如下面程序。
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# 创建 Item 对象，将之赋值给 im 变量


im = Item('鼠标', 298)
# 打 im 用的 It em 对象
print(im)
print(im.__repr__())


class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    # 重写 re pr （）方法，用于实现 Apple 对象的“自我描述”

    def __repr__(self):
        return "Apple[color=" + self.color + ', weight=' + str(self .weight)+']'


a = Apple('红色', 5.68)
# 打印 Apple 对象
print(a)


