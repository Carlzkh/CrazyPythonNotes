"""
6. 定义 fn(n ）函数，该函数返回n的阶乘
"""


def fn(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


print(fn(1))
print(fn(2))
print(fn(3))
print(fn(4))
