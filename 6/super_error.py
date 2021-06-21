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
        print('我是 个顾客，我的爱好是：%s，地址:%s' % (self.favorite, self.address))


# Manager 继承了 Employee Customer
class Manager (Employee, Customer):
    pass


m = Manager(25000)
m.work()  # ①
# m.info()  # ② 会报错，Manager类创建的对象没有favorite和address属性，只有继承自Employee类的salary属性。

