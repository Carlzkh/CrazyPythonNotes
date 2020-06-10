"""
下面粗体字代码使用 type （） 定义了 Dog 类。在使用 type（） 定义类时可指定三个参数。
》参数一：创建类名。
》参数二：该类继承的父类集合。
    由于 Python 支持多继承，因此此处使用元组指定它的多个父类。即使实际只有一个父类， 需要使用元组语法（必须要多一个逗号〉。
》参数三：该宇典对象为 豆类绑定 类变量和方法。其中字典 key 是类变量或方法名
    如果字典的 value 是普通值，那就代表类变量 如果 字典的 value 是函数，则代表方法
由此可见，上面粗体字代码定义了 Dog 该类继承了 object ，还为 Dog类定义了一个
walk()方法和一个age类变量。
"""


def fn(self):
    print('fn 函数')
# 使用 type （）定义 Dog


Dog = type('Dog', (object,), dict(walk=fn, age=6))
# 创建 Dog 对象
d = Dog()
# 分别查看 Dog 类型
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)

'''
从上面的输出结果可以看出，使用 type()函数定义的类与直接使用 class 定义的类并没有任何
区别。事实上 Python 解释器在执行使用 class 定义的类时，其实依然是使用 type()函数来创建类的
。因此，无论通过哪种方式定义类，程序最终都是创建一个type实例的。
'''
