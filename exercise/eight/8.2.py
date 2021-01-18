"""
2. 自定义 1个序列，该序列按顺序包含所有三位数（如 100 101 102 。要 提供序列的
各种操作方法。
"""


def check_key(key):
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError("索引值必须是非负整数")
    if key >= 900:
        raise IndexError('索引值不能超过900')


class ThreeDigits:
    def __init__(self):
        self.__digits = [x for x in range(100, 1000)]

    def __len__(self):
        return 900

    def __getitem__(self, key):
        check_key(key)
        return self.__digits[key]

    def __contains__(self, item):
        if item in self.__digits:
            return True
        else:
            return False

    def __setitem__(self, key, value):
        check_key(key)
        self.__digits[key] = value

    def __delitem__(self, key):
        check_key(key)
        del self.__digits[key]


puke = ThreeDigits()
print(puke.__dict__)
print(puke.__contains__(100))
puke.__setitem__(899, 'kk')
print(puke._ThreeDigits__digits)  # 私有变量（__digits）可以通过下划线加类名来访问，不可以直接访问
print(puke.__dir__())


