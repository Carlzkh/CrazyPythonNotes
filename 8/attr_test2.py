class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写__setattr__()方法对设置的属性值进行检查,必须写前后的双下划线
    # __setattr__()和setattr()完全不同，一定要注意前后的双下划线
    def __setattr__(self, name, value):
        # 如果正在设置 name 属性
        if name == 'name':
            if 2 < len(value) <= 8:
                self.__dict__['name'] = value
            else:
                raise ValueError('name的长度必须在2-8之间')
        elif name == 'age':
            if 10 < value < 60:
                self.__dict__['age'] = value
            else:
                raise ValueError('age的值必须在10-60之间')


u = User('crazy', 24)
print(u.name)
print(u.age)
# u.name = 'disappointment'  # 引发异常
# u.age = 2  # 引发异常
