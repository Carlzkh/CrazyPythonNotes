"""
3.提供 1个字符串元组，程序要求元组中每一个元素的长度都在 5~20 之间：否则， 程序
发异常。
"""


class LengthException(BaseException):
    pass


try:
    str1 = input('输入一个字符串元组：')
    list1 = str1.split(' ')
    tuple1 = tuple(list1)
    for i in range(len(tuple1)):
        if 5 <= len(tuple1[i]) <= 20:
            pass
        else:
            raise LengthException('元素长度不在5~20之间')
except Exception as e:
    print(e.args)
