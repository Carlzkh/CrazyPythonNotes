"""
使用未绑定方法（类名调用实例方法）的方式，调用被重写的父类方法

"""


class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')


class SubClass(BaseClass):
    # 重写父类的 foo 方法
    def foo(self):
        print('子类重写父类中的foo方法')

    def bar(self):
        print('执行bar方法')
        # 直接执行foo方法，将会调用子类重写之后的foo方法
        self.foo()
        # 使用类名调用实例方法(未绑定方法)调用父类被重写的方法
        BaseClass.foo(self)  # 类名调用方法需要显示的绑定参数self（其实无论写啥都可以，self可以看成没有被使用的普通参数）


sc = SubClass()
sc.bar()
