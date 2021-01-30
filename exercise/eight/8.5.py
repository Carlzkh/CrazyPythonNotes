"""
5. 定义 1个生成器，可依次返回1, 2, 3, …的阶乘
factorial:阶乘
"""


def factorial():
    base = 2
    factorial_ = 1
    while base <= 10:
        factorial_, base = base * factorial_, base + 1
    # base += 1
        yield factorial_


card = factorial()
print(list(card))
