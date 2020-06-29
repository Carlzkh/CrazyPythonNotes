"""
1. 自定义 个序列，该序列按顺序包含 52 张扑克牌，分别是黑桃、红心、草花、方块的2-A
要求：提供序列的各种操作方法

"""


class PlayingCard:
    poker_suit1 = '黑桃'
    poker_suit2 = '红心'
    poker_suit3 = '草花'
    poker_suit4 = '方块'
    list1 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, hard_cards):
        self.hard_cards = hard_cards
        # self.number = number

    def __setitem__(self, key, value):
        self.hard_cards[key] = value

    def __getitem__(self, item):
        if item in self.hard_cards:
            return self.hard_cards[item]
        else:
            print('您手牌中没有此牌')
            return None

    def __len__(self):
        return len(self.hard_cards)

    def __contains__(self, item):
        for i in range(1, 4):
            if item in self.hard_cards[i]:
                print('存在此牌')
                return True
        return False

    def __delitem__(self, key):
        del self.hard_cards[key]


hard_cards1 = {1: '黑桃2', 2: '红心3', 3: '梅花4', 4: '方块5'}
player1 = PlayingCard(hard_cards1)
print(len(player1))
print(player1.__len__())
print(hard_cards1[1])
# print(hard_cards[5]) 报错
print(player1.__getitem__(2))
print(player1.__getitem__(5))
print(player1.__contains__('红心3'))
print(player1.__contains__('红心4'))


# 参考答案：没实现contains()
def check_key(key):
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError('索引值必须是非负整数')
    if key >= 52:
        raise IndexError('索引值不能超过%d' % 52)


class CardSeq:
    def __init__(self):
        self.flowers = ('♠', '♥', '♣', '♦')
        self.values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        self.__changed = {}
        self.__deleted = []

    def __len__(self):
        return 52

    def __getitem__(self, key):
        check_key(key)
        # 如果在self.__changed中找到已经修改后的数据
        if key in self.__changed:
            return self.__changed[key]
        # 如果key在self.__deleted中，说明该元素已被删除
        if key in self.__deleted:
            return None
        # 否则根据计算规则返回序列元素
        flower = key // 13
        value = key % 13
        return self.flowers[flower] + self.values[value]

    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key] = value

    def __delitem__(self, key):
        check_key(key)
        # 如果__deleted列表中没有包含被删除key，添加被删除的key
        if key not in self.__deleted:
            self.__deleted.append(key)
        # 如果__changed中包含被删除key，删除它
        if key in self.__changed:
            del self.__changed[key]

    def __contains__(self, item):
        for i in range(1, 51):
            if i in self.__changed:
                if item in self.__changed[i]:
                    print('存在此牌')
                    return True
        return False


if __name__ == '__main__':
    cq = CardSeq()
    print(len(cq))
    print(cq[2])  # '♠4'
    print(cq[1])  # '♠3'
    # 修改cq[1]元素
    cq[1] = '♣2'
    # 打印修改之后的cq[1]
    print(cq[1])  # '♣2'
    # 删除cq[1]
    del cq[1]
    print(cq[1])  # None
    # 再次对cq[1]赋值
    cq[1] = '♦5'
    print(cq[1])  # ♦5
    cq.__contains__('♦5')
    print(cq.__contains__('方块5'))
