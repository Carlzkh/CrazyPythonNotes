class User:
    def walk(self):
        print(self, 'is walking slowly')


User.walk('Carl')  # 不传参会报错,传参会把参数赋给self变量
u = User()  # 实例化对象
User.walk(u)  # 手动绑定对象到实例方法，结果等于u.walk()
u.walk()  # 对象调用方法，绑定后就不需要传递self参数了

















