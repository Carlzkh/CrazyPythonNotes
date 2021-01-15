"""
1. 自定义 1个序列，该序列按顺序包含 52 张扑克牌，分别是黑桃、红心、草花、方块的2~A
要求：提供序列的各种操作方法
"""
import collections

Card = collections.namedtuple('Card', ['value', 'color'])


def check_key(key):
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError("索引值必须是非负整数")
    if key >= 52:
        raise IndexError('索引值不能超过52')


class PlayingCards:
    colors = 'spades hearts clubs diamonds'.split(' ')
    values = [str(n) for n in range(2, 11)] + list('JQKA')

    def __init__(self):
        self.__cards = [Card(value, color) for color in self.colors
                        for value in self.values]

    def __len__(self):
        return 52

    def __getitem__(self, key):
        check_key(key)
        return self.__cards[key]

    def __contains__(self, item):
        if item in self.__cards:
            return True
        else:
            return False

    def __setitem__(self, key, value):
        check_key(key)
        self.__cards[key] = value

    def __delitem__(self, key):
        check_key(key)
        del self.__cards[key]


puke = PlayingCards()
print(puke.__dict__)
