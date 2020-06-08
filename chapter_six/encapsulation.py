"""
encapsulation：封装
"""


class User:
    def hide(self, name):
        self.name = name
        print('示范隐藏的 hide 方法')

    def getname(self):
        return self.__name

    def setname (self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在于3-8之间')
        self.__name = name
    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户名年龄必须在 18 70 之间')
        self.__age = age

    def getage(self):
        return self.__age
    age = property(getage, setage)
# 创建 User 对象


u = User()
# 对 name 属性赋值，实际上调用 setname （）方法
u.name = 'fwp'  # 引发 ValueError 错误：用户名长度必须在 3-8 之间











