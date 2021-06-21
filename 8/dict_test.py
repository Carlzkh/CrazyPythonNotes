"""
__dict__属性用于查看对象内部存储的所有属性名和属性值组成的字典
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 29.8)
print(im.__dict__)
# 通过__dict__访问 name 属性
print(im.__dict__['name'])
# 通过__dict__访问 price 属性
print(im.__dict__['price'])
# __dict__返回值，可以通过修改字典的方式进行修改
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name)
print(im. price)
