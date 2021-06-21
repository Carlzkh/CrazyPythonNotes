class User:
    def walk(self):
        print(self, 'is walking slowly')


# User.walk(1)  # 不传参会报错,传参会把参数赋给self变量
u = User()  # 实例化对象
# User.walk(u)  # 手动绑定对象到实例方法，结果等于u.walk()
u.walk()  # 对象调用方法，绑定后就不需要传递self参数了


def foo():
    print('这是类之外的foo')


bar = 'outclass'


class Bird:
    def foo(self):
        print('这是Bird类中的foo')

    bar = 'in_class'


foo()
print(bar)

Bird.foo(2)
print(Bird.bar)
print('==========================================================================')


def decorator(fn):
    # 定义 个嵌套函数
    def barr(*args):
        print('＝＝＝1＝＝＝', args)
        n = args[0]
        print('＝＝＝2＝＝＝', n * (n-1))
        # 查看传给 foo 函数的 fn 函数
        print(fn.__name__)
        fn(n * (n - 1))
        print(' * ' * 15)
        return fn(n * (n - 1))
    return barr


'''下面的装饰效果相当于 foo(my_test)
my test 将会被替换（装饰〉成该语句的返回值
由于 foo （）函数返回 bar 函数，因此 funB 就是 bar
'''


@decorator
def my_test(a):
    print('==my test 函数＝＝', a)


# 打印 my test 函数，：每看到实际上是 bar 函数
print(my_test)
# <function foo . <locals>.bar at Ox00000000021FABF8>
# 下面代码看上去是调用 my_test （），其实是调用 bar （）函数
my_test(10)
my_test(6, 5)



