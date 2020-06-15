"""
对于＿getattr （）方法：它只处理程序访问指定属性且该属性不存在的情形。比如程序访问
width height 属性， Rectangle 对象本身包含该属性，因此该方法不会被触发。所以重写
该方法只需处理我们需要“合成”的属性（比如 ze ），假如程序试图访问其他不存在的
属性，当然直接引发 AttributeError 异常即可。
〉对于__setattr__()方法，只要程序试图对指定属性赋值时总会触发该方法，因此无论程序是对
width height 属性赋值，还是对 size 属性赋值，该方法都会被触发。所以重写该方法既
要处理对 ize 性赋值的情形，也要处理对 width height 属性赋值的情形。尤其是处理对
width height 属性赋值的时候，千万不要在__setattr__()方法中再次对 width height 赋值，
因为对这两个属性赋值会再次触发__setattr__()方法，这样会让程序陷入死循环中。

"""


class Rectangle:
    def __init__(self, width , height):
        self.width = width
        self.height = height
    def __setattr__(self, name , value):
        print('一一设置%s属性一一' % name)
        if name == 'size':
            self.width, self.height = value
        else :
            self.__dict__[name] =value
    def __getattr__(self, name):
        print('一一读取%s属性一一' % name)
        if name =='size':
            return self.width, self.height
        else:
            raise AttributeError
    def __delattr__(self, name):
        print('一一删除在%s属性一一' % name)
        if name == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0


rect = Rectangle(3, 4)
print(rect.size)
rect.size = 6, 8
print(rect.width)
del rect .size
print(rect.size)
