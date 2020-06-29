class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def valid_login(self):
        print('验证%s登录' % self.name)


# 定义 Role
class Role:
    def __init__(self, name):
        self.name = name

    # 定义→call＿方法
    def __call__(self):
        print('执行 Role 对象')


u = User('one', 'two')
# 判断 .name 是否包含__call__方法，即判断它是否可调用
print(hasattr(u.name, '__call__'))  # False
# 判断 password 是否包含__call__方法，即判断它是否可调用
print(hasattr(u.password, '__call__'))  # False
# 判断 va li dLogin 是否包含__call__方法，即判断它是否可调用
print(hasattr(u.valid_login, '__call__'))  # True

r = Role('理员')
# 直接调用 Role 对象，就是调用该对象的 call 方法
r()


def foo():
    print('--foo函数--')


# 下面示范了通过两种方式来调用 foo()函数
foo()
foo.__call__()
