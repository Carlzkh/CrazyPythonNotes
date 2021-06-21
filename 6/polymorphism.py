"""
多态

"""


class Canvas:
    def draw_pic(self,shape):
        print('--绘制图形--')
        shape.draw(self)


class Rectangle:
    def draw(self, canvas):
        print('%s绘制矩形' % canvas)


class Triangle:
    def draw(self, canvas):
        print('%s绘制三角形' % canvas)


class Circle:
    def draw(self, canvas):
        print('%s绘制圆形' % canvas)


c = Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())


'''
> issubclass(els , class or_ tuple ):检查 els 是否为后 个类或元组包含 多个类中任意类 子类。
> isinstance(obj , class or_ tuple ):检查 均是否为后 个类或元组包含的多个类中任意类的对象
'''
print(issubclass(Canvas, (Canvas, Rectangle)))

'''
查看所有父类的属性：__bases__
'''


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print('A的所有父类', A.__bases__)
print('B的所有父类', B.__bases__)
print('C的所有父类', C.__bases__)


