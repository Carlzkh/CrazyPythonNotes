"""
slots属性值是一个元组，它限制了类的实例能动态添加的变量和方法，但是并不限制类本身动态添加变量和方法

"""


class Dog: 
    __slots__ = ('walk', 'age', 'name')
    def __init__(self, name) :
        self.name = name
    def test() :
        print(' 预先定义的 test 方法')


d = Dog('Snoopy')
from types import MethodType 
# 只允许为实例动态添加 walk age name 这三个属性或方法
d.walk = MethodType(lambda self: print('%s慢慢地走' % self.name), d)
d.age = 5
d.walk()
# d.foo = 30 # AttributeError
#Dog.walk()