"""
8. 定义 fn(n）函数，该函数返回 1个包含n个不重复的 0~100 之间整数的元组
"""
import random
list_init = [x for x in range(101)]
# print(list_init)


def fn(n):
    target_list = []
    for i in range(n):
        element = random.choice(list_init)
        target_list.append(element)
        list_init.remove(element)
    return tuple(target_list)


print(fn(1))
print(fn(5))
print(fn(10))
print(fn(46))
