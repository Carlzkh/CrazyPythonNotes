"""
inherit：继承

"""


class Fruit:
    def info(self):
        print('我是个水果!重%g克' % self.weight)


class Food:
    def taste(self):
        print('不同食物的口感不同,我是%s' % self.name)


# 定义 Apple 类，继承了 Fruit 类和 Food
class Apple(Fruit, Food):
    pass


# 创建 Apple 对象
a = Apple()
a.weight = 5.6
a.name = 'apple'
# 调用 Apple 对象 info 方法
a. info()
# 调用 Apple 对象的 taste （）方法
a . taste()
