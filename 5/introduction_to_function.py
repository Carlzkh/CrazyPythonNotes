"""
函数入门
"""
'''
1、定义函数、调用函数
'''


def my_max(x, y):
    z = x if x > y else y
    return z


def my_max2(x, y):
    return x if x > y else y


result = my_max(1, 2)
print(result)
print(my_max2(1, 2))


'''
2、函数文档
'''


def my_max3(x, y):
    """
    获取两数的最大值
    :param x:
    :param y:
    :return:
    """
    z = x if x > y else y
    return z


# help(my_max3(1, 2))
print(my_max3.__doc__)


'''
3、多个返回值
返回列表，或多个变量
直接返回多个变量，python会自动封装成元组，可以利用序列解包直接用多个变量接收
'''


def agv_and_sum(list1):
    sum1 = 0
    count = 0
    for i in list1:
        if isinstance(i, int) or isinstance(i, float):
            sum1 += i
            count += 1
    return sum1, sum1 / count


list2 = [1, 2, 0.8, 0.2, 'a']
tuple1 = agv_and_sum(list2)
a, b = agv_and_sum(list2)
print(tuple1, a, b, sep='\n')


'''
4、递归函数
在函数体中调用函数自身
递归一定要向已知的方向进行，否则会形成类似死循环的无限递归
'''


def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n-1) + fn(n-2)


print(fn(10))
















