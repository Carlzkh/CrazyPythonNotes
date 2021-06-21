"""
这是我们编写的第 个模块，该模块包含以下内容
my book 字符串变量
say hi 简单的函数
User ：代表用户的类

可借助于所有模块内置的__name__变量进行区分，如果直接使用 python 令来运行一个
模块， __name__变量的值为 __main__ ；如果该模块被导入其他程序中，__name__变量的值就是模
块名。因此，如果希望测试函数只有在使用 python 命令直接运行时才执行，则可在调用测试函数
时增加判断：只有当__name__属性为__main__时才调用测试函数。
"""

print('这是module1')
my_book = '疯狂Python讲义'


def say_hi(user):
    print('%s, 您好，欢迎学习 Python' % user)


class User:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('%s正在慢慢地走路' % self.name)

    def __repr__(self):
        return 'User[name=%s]' % self.name


# ＝＝＝以下部分是测试代码＝＝＝
def test_my_book():
    print(my_book)


def test_say_hi():
    say_hi('孙悟空')
    say_hi(User('Charlie'))


def test_user():
    u = User('白骨精')
    u.walk()
    print(u)


# 增加如下__name__ == '__main__'的判断，在导入的时候就不会执行下面的代码了，因为导入时__name__等于模块名
if __name__ == '__main__':
    test_my_book()
    test_say_hi()
    test_user()


