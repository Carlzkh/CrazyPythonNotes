"""
9. 定义 fn(n ）函数，该函数返回 1个包含 n个不重复的大写字母的元组
"""
import random


def fn(n):
    list_init = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    target_list = []
    for i in range(n):
        element = random.choice(list_init)
        target_list.append(element)
        list_init.remove(element)
    return tuple(target_list)


print(fn(1))
print(fn(5))
print(fn(10))
print(fn(24))

