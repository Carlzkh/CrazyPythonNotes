"""
super函数用来调用父类的构造方法，继承的特性也适用于构造方法，当然重写也是一样的

"""


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是 ：%d' % self.salary)


class Customer:
    def __init__(self, favorite, address):
        self .favorite = favorite
        self.address = address

    def info(self):
        print('我是个顾客，我的爱好是：%s，地址:%s' % (self.favorite, self.address))


# Manager 继承了 Employee Customer
class Manager (Employee, Customer):
    def __init__(self, salary, favorite, address):
        print('一Manager的构造方法——')
        # 通过super （）函数调用父类的构造方法
        super().__init__(salary)
        # 与上一行代码的效果相同
        # super(Manager, self) .__init__(salary)  # 与super().__init__(salary)只用写一个
        # 使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, address)


m = Manager(3600, '炒股', 'white house')
m.work()  # ①
m.info()  # ② 与super_error相比，修改了Manager类，以此可以使用其他父类的属性

