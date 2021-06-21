"""
提供一个字符串元组，程序要求元组中每一个元素的长度都在 5-20 之间：否则， 程序触发异常。
"""


class CarlException(Exception):
    pass


tuple1 = ('1', 'sad', 'good')
try:
    for i in range(len(tuple1) - 1):
        if not (5 < len(tuple1[i]) < 20):
            raise CarlException('存在字符长度不在5-20之间')
except Exception as e:
    print('异常', e)


# 参考答案
def fn(tp):
    for e in tp:
        if not isinstance(e, str):
            raise ValueError('所有元素必须是字符串')
        if not (20 >= len(e) >= 6):
            raise ValueError('字符串的长度必须在6～20之间')
    print(tp)


if __name__ == '__main__':
    fn(('fkjava', 'crazyit'))
    #    fn((20,))
    fn(('fkjavafkjavafkjavafkjava'))

