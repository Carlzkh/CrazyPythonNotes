class Person:
    """ 定义一个person类"""
    hair = 'black'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # @staticmethod    设置静态方法的话，self也需要传值
    def say(self, words):  # 不使用self属性的话，函数会被建议为静态函数，所以函数名下有下划线
        print(words)

    @staticmethod
    def run(self, words):
        print(words)

    @staticmethod
    def eat(food):
        print(food)


a = Person('Carl', 18)
print(a.name, a.age)
a.say('hello')
a.run('hello', 7)
a.eat('apple')
a.height = 180  # 为对象新加实例变量
del a.name  # 删除对象的实例变量
print(a.height)
# print(a.name)  # 对象的实例变量被删除，访问会报错


def info(self):
    print('====================')


a.foo = info
a.foo('i')


class User:
    def walk(self):
        print(self, 'is working slowly')


User.walk(1)  # 不传参会报错,传参会把参数赋给self变量
u = User()  # 实例化对象
User.walk(u)  # 手动绑定对象到实例方法，结果等于u.walk()
u.walk()  # 对象调用方法，绑定后就不需要传递self参数了












