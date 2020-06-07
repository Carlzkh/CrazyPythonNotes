"""
多继承：多个父类有相同的方法名时：
如果多个父类中包含了同名的方法，此时会发生什么呢？
此时排在前面的父类中的方法会“遮蔽”排在后面的父类中的同名方法
"""


class Item:
    @staticmethod
    def info(self):
        print('Item中方法 ， 这是 个商')


class Product:
    @staticmethod
    def info(self):
        print('Product中方法：这是一个工业')


class Mouse(Item, Product):
    pass


# Mouse类的对象以Mouse类的继承顺序优先使用前面的父类的方法，后面父类的同名方法会被覆盖，不会执行
m = Mouse()
m.info(2)  # info方法被装饰器装饰成了静态方法，self参数就是正常参数，需要传值
