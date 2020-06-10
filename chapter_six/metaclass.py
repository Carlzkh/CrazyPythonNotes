"""
如果希望创建某 类全部具有某种特征， 则可通过 metaclass 来实现。使用 metaclass 可以在创建类时动态修改类定义
为了使用 metaclass 动态修改类定义，程序需要先定义 metaclass, metaclass 应该继承 type 类，
并重写__new__（）方法
下面程序定义了 一个 metaclass

"""


# 定义 ItemMetaClass ，继承 type
class ItemMetaClass(type):
    # el 表被动态修改的类
    # name 代表被动态修改的类名
    # bases 代表被动态修改的类的所有父类
    # attr 代表被动态修改的类的所有属性、方法组成的字典
    def __new__(mcs, name, bases, attrs):
        # 为该类动态添加一个 cal price 方法
        attrs['call_price'] = lambda self: self.price * self.discount
        return type.__new__(mcs, name, bases, attrs)


class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount
    # 定义 Cell Phone


class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


b = Book('疯狂Python讲义 ', 89)
b.discount = 0.76
# 创建 Book 对象的 cal price （）方法
print(b.call_price())
cp = CellPhone(2399)
cp.discount = 0.85
# 创建 Cell Phone 对象的 cal_price （）方法
print(cp.call_price())






