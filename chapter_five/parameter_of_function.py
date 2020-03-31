"""
函数的参数
"""
'''
1、关键字参数
函数调用时，参数按顺序赋值，叫做位置参数
指定了变量名从赋值方式叫关键字参数
关键字参数必须放在位置参数的后面
'''


def girth(width, height):
    """
    矩形周长

    """
    print('width:', width, end='\t')
    print('height:', height)
    return 2 * (width + height)


girth(1, 2)
girth(2, 1)
girth(width=1, height=2)
girth(height=2, width=1)
girth(1, height=2)


'''
2、默认值参数：定义函数的时候为形参赋值（类似关键字参数，关键字参数是调用的时候，默认值参数是定义的时候）
默认值参数应定义在形参的最后，防止位置参数改变了默认值参数
'''


def print_triangle(char, height=5):
    for i in range(1, height+1):
        for j in range(height - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print(char, end='')
        print()


print_triangle('@')
print_triangle('@', 3)


'''
3、参数收集，可变长参数
可变长普通参数，：*args，python把接收到的所有元素当成元组处理
可变长关键字参数：**kwargs，python把接收到的所有元素当成字典处理
参数列表中都只能有一个，位置随便，若还有其他参数在可变长参数后的话，建议使用关键字参数，因为位置参数会被当成可变长参数的一部分
'''


def test(*books, x, y, z=3, **scores):
    print(books)
    print(x, y, z)
    print(scores)


test('疯狂python', '疯狂Java', 2, x='x', y='y', 语文=89, 数学=99)


'''
4、逆向参数收集：把列表、元组、字典等对象里的元素赋值给形参
在列表、元组前加*
在字典前加**
'''


def test(name, message):
    print(name)
    print(message)


list1 = ['Carl', 'what\'s your name']
test(*list1)


def bar(name, price, desc):
    print("名字是：", name)
    print("价格是：", price)
    print("拿什么：", desc)


dict1 = {'name': '疯狂python', 'price': 89, 'desc': '社么'}
bar(**dict1)


'''
5、参数传递机制：值传递
'''














