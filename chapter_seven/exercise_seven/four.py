"""
4. 提示用户输入 x1, y1, x2, y2, x3, y3 六个数值，分别代表 三个点的坐标，程序判断这 三个点
是否在同一条直线上。要求 使用异常处理机制处理用户输入的各种错误情况，如果三个点不在同
条直线上，则程序出现异常
"""


class carlException(Exception):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def point_distance(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


print('输入六个值，代表三个点的坐标')
x1 = int(input('x1'))
y1 = int(input('y1'))
x2 = int(input('x2'))
y2 = int(input('y2'))
x3 = int(input('x3'))
y3 = int(input('y3'))

a = Point(x1, y1)
b = Point(x2, y2)
c = Point(x3, y3)
ab = a.point_distance(a, b)
bc = a.point_distance(b, c)
ac = a.point_distance(a, c)
max_side = max(ab, bc, ac)
try:
    if max_side == ab:
        if ab == bc + ac:
            print('abc三点在一条直线上')
        else:
            raise carlException('自定义错误')
    elif max_side == ac:
        if ac == ab + bc:
            print('abc三点在一条直线上')
        else:
            raise carlException('自定义错误')
    else:
        if bc == ac + ab:

            print('abc三点在一条直线上')
        else:
            raise carlException('自定义错误')
except Exception as e:
    print('abc三点不在一条直线上', e)


# 参考答案
while True:
    st = input("请输入3个点的x、y值(空格隔开): ")
    if st == 'exit':
        import sys
        sys.exit(0)
    try:
        x1_st, y1_st, x2_st, y2_st, x3_st, y3_st = st.split()
        x1, y1, x2, y2, x3, y3 = float(x1_st), float(y1_st), float(x2_st), float(y2_st), float(x3_st), float(y3_st)
        if x1 == 0 and x2 == 0 and x3 == 0:
            print('处于同一条直线')
        elif 0 in (x1, x2, x3):
            print('不处于同一条直线')
        elif y1 / x1 == y2 / x2 and y1 / x1 == y3 / x3:
            print('处于同一条直线')
        else:
            print('不处于同一条直线')
    except:
        print('必须输入6个空格隔开的数')

