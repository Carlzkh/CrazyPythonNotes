"""
~ hasattr(obj , name）：检查 obj 对象是否包含名为 name 的属性或方法
~ getattr(object, name[,default])：获取 object 对象中名为 name的属性、属性值。
~ setattr( obj, name, value ，／）：将 obj 对象的 name 属性设为 value


"""


class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times

    def info(self):
        print('一条简单的评论,内容是:%s' % self.detail)


c = Comment('疯狂 Python 讲义很不错', 20)
# 判断是否包含指定的属性或方法
print(hasattr(c, 'detail'))
print(hasattr(c, 'view_times'))
print(hasattr(c, 'info'))
# 获取指定属性的属性值
print(getattr(c, 'detail'))
print(getattr(c, 'view_times'))
# 由于 info 是方法，故下面代码会提示 name info is not defined
# print (getattr(c, info, '默认值'))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
# 输出重新设置后的属性值
print(c.detail)
print(c.view_times)


def bar():
    print('一个简单的bar方法')


# 将 info 方法设为 bar 函数
setattr(c, 'info', bar)
c.info()




