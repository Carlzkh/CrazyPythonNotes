"""
>__len__(self)该方法的返回值决定序列中元素的个数。

>__getitem__(self, key)：该方法获取指定索引对应的元素。
该方法的 key 应该是整数值或slice对象，否则该方法会引发 KeyError异常。

>__contains__(self, item):该方法判断序列是否包含指定元素。

>__setitem__(self, key, value)该方法设置指定索引对应的元素。
该方法的 key 应该是整数值或slice对象，否则该方法会 KeyError 异常。

>__delitem__(self, key)该方法删除指定索引对应的元素。

如果程序要实现不可变序列（程序只能获取序列中的元素，不能修改），只要实现上面前3个方法就行；
如果程序要实现可变序列（程序既能获取序列中的元素，也可修改）， 需要实现上面5个方法。

"""


def check_key(key):
    """该函数将会负责检查序列的索引，该索引必须是整数值，否则引发 TypeError 异常
    且程序要求索引必须为非负整数值，否则引发 IndexError 异常"""
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError('索引值必须是非负整数')
    if key >= 26 ** 3:
        raise IndexError('索引值不能超过%d' % 26 ** 3)


class StringSeq:
    def __init__(self):
        # 用于存储被修改的数据
        self.__changed = {}
        # 用于存储己删除元素的索寻｜
        self.__deleted = []

    def __len__(self):
        return 26 ** 3

    def __getitem__(self, key):
        # 根据索引获取序列中元素
        check_key(key)
        # 如果在 self. changed 中找到修改后的数据
        if key in self.__changed:
            return self.__changed[key]
        # 如果 key self._deleted 中，说明该元素已被删除
        if key in self.__deleted:
            return None
        # 否则根据计算规则返回序列元素
        three = key // (26 * 26)
        two = (key - three * 26 * 26) // 26
        one = key % 26
        return chr(65 + three) + chr(65 + two) + chr(65 + one)

    def __setitem__(self, key, value):
        # 根据索引修改序列中元素
        check_key(key)
        # 将修改的元素以 key value 对的形式保存在 changed
        self.__changed[key] = value

    def __delitem__(self, key):
        # 根据索引删除序列中元素
        check_key(key)
        # 如果＿deleted 列表中没有包含被删除的 key ，则添加被删除的 key
        if key not in self.__deleted:
            self.__deleted.append(key)
        # 如果＿changed 中包含被删除的 key 则删除它
        if key in self.__changed:
            del self.__changed[key]
# 创建序列


sq = StringSeq()
# 获取序列的长度，实际上就是返回__len__()方法的返回值
print(len(sq))
print(sq[26*26])
# 印修改之前的 sq [1]
print(sq[1])  # 'AAB'
# 修改 sq[1]元素
sq[1] = 'one'
# 印修改之后的 sq[1]
print(sq[1])
# 删除 sq[1]
del sq[1]
print(sq[1])
# 再次对 sq[1］赋值
sq[1] = 'crazy'
print(sq[1])  # crazy


for i in range(26 ** 3 - 1):
    print(sq[i])

print(chr(65))
