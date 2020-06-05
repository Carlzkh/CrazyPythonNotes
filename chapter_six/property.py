class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first + ',' + self.last

    def set_fullname(self, fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]
    # 使用 property （） 函数定义 fullname 属性，只传入两个参数
    # 该属性是 卖写属性，但 能删除
    fullname = property(getfullname, set_fullname)


u = User('悟空', '孙')
# 访 fullname 属性
print(u.fullname)
# 对 fullname 属性赋值
u.fullname = '八戒,朱'
print(u.first)
print(u.last)


# property装饰器


class Cell:
    # 为 state 属性设置 setter 方法
    def __init__(self, state):
        self._state = state

    # 使用自property 修价方法， 当于为该属性设置 getter 方法
    @property
    def state(self):
        return self._state
    # 为 state 属性设置 setter 方法

    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    # 为 is_dead 属性设置 getter 方法
    # 只有 getter 方法的属性是只读属性
    @property
    def is_dead(self):
        return not self.state.lower() == 'alive'


c = Cell('live')
# 修改 state 属性
print(c.state)
c.state = 'Alive'
# 访问 state 属性
print(c.state)
# 访问 is dead 属性
print(c.is_dead)



