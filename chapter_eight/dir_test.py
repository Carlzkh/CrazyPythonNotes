"""
__dir__:返回对象的所有属性和方法
"""


class Item:
    def __init__(self, name, price):
        self . name = name
        self .price = price

    def info(self):
        pass
# 创建 Item 对象 将之赋值给 im 变量


im = Item('鼠标', 29.8)
print(im.__dir__())  # 返回所有属性（包括方法〉组成的列表
print(dir(im))  # 返回所有属性（包括方法〕排序之后的列表
