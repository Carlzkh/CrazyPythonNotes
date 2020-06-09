"""
动态属性与slots

"""


class Cat:
    def __init__(self, name):
        self.name = name


def walk_func(self):
    print('%s慢慢地走过一片草地' % self.name)


d1 = Cat('Garfield')
d2 = Cat('Kitty')
# d l . wa l k () # Attribut eErro r
# 为 Cat 动态添加 walk （）方法，该方法的第 个参数会自动绑定
Cat.walk = walk_func  # ①
# dl d2 调用 walk （）方法
d1.walk()
d2.walk()
walk_func(d1)
