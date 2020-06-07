"""
重写父类方法：子类用相同的方法名重新定义方法的内容，子类对象调用时，只会执行子类的方法，父类的同名方法将不执行
这种子类包含与父类同名的方法的现象被称为方法重写（ Override ），也被称为方法覆盖。可
以说子类重写了父类的方法，也可以说子类覆盖了父类的方法
"""


class Bird:
    # Bird 类的 fly （）方法
    def fly(self):
        print('我在天空里自由自在地飞翔')


class Ostrich(Bird):
    # 重写 Bird 类的 fly （）方法
    def fly(self):
        print('我只能在地上奔跑')
# 创建 Ostrich 对象


os = Ostrich()
# 执行 Ostrich 对象的 fly （）方法，将输出 我只能在地上奔跑 ．．
os.fly()




