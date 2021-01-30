"""
10. 定义一 fibonacci(n) 函数，该函数返回包含n个元素 斐波那契数列的列表。再使用 lambda
表达式定义 1个平方函数，程序最终输出斐波那契数列的前 n 个元素的平方值。
"""


def fibonacci(n):
    list11 = []
    first = 0
    sec = 1
    for i in range(n):
        first, sec = sec, first + sec
        list11.append(first)
    return list11


list1 = fibonacci(10)
print(list1)
# list2 = []
# for j in list1:
#     x = lambda j: j * j
#     list2.append(x)
# print(list2)
y = map(lambda x: x*x, list1)
print(y.__dir__())  # y是一个map对象，只有方法，没有属性
print([e for e in y])
