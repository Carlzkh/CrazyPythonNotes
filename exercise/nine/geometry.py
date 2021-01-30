"""
geometry模块的文档说明：在该模块下定义了 print_triangle(n)和 print_diamond(n)两个函数，分
别用于在控制台用星号打印三角形和菱形！
"""


def print_triangle(n):
    """
    输出n行的三角形
    :param n:
    :return:
    """
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))


def print_diamond(n):
    """
    输出2*n+1行的菱形！
    :param n:
    :return:
    """
    if n % 2 != 0:
        for i in range(1, n + 1):
            if i < (n + 1) / 2:
                print(' ' * ((n + 1) // 2 - i), end='')
                print('*' * (2 * i - 1))
            elif i == (n + 1) / 2:
                print('*' * (2 * i - 1))
            else:
                print(' ' * (i - (n + 1) // 2), end='')
                print('*' * (2 * (n - i) + 1))
    else:
        print('用户输入的是偶数，不能打印！')


