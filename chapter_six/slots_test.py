"""
slots属性值是一个元组，它限制了类的实例能动态添加的变量和方法，但是并不限制类本身动态添加变量和方法

"""
from types import MethodType


class Dog: 
    __slots__ = ('walk', 'age', 'name')

    def __init__(self, name):
        self.name = name

    @staticmethod
    def test():
        print(' 预先定义的 test 方法')


d = Dog('Snoopy')

# 只允许为实例动态添加 walk age name 这三个属性或方法
d.walk = MethodType(lambda self: print('%s慢慢地走' % self.name), d)
d.age = 5
d.walk()
# d.foo = 30 # AttributeError
# Dog.walk()

# 不妨碍类添加动态变量
Dog.legs = 4
print(d.legs)
# 不妨碍类添加动态方法
Dog.bar = lambda self: print('abc')  # AttributeErr
d.bar()


# slots对派生的子类没有用
class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    pass


gd = GunDog('Puppy')
# 完全可以为 Gun Dog 实例Z;/J 态添加属性
gd.speed = 99
print(gd.speed)

'''
正如从上面代码所看到的， Dog 子类 GunDog 实例完全可以动态添加 speed 属性，这说明
slots 属性指定的限制只对当前类起作用。
如果要限制子类的实例动态添加属性和方法，则需要在子类中也定义 slots 属性，这样，子
类的实例允许动态添加属性和方法就是子类的＿slots_ 元组加上父类的＿slots＿元组的和。
'''
