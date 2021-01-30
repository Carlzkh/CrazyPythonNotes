"""
8. 自定义代表 克牌的 Card 类（包括花色和牌面值），为 Card 类提供自定义的比较大小的运
算符支持 大小比较标准是先比较牌面值，如果牌面值相等则比较花色，花色大小规则为 黑桃＞
hx＞草花＞方块
"""


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        replace_value = {
            '2': 0,
            '3': 1,
            '4': 2,
            '5': 3,
            '6': 4,
            '7': 5,
            '8': 6,
            '9': 7,
            '10': 8,
            'J': 9,
            'Q': 10,
            'K': 11,
            'A': 12,
            '小王': 13,
            '大王': 14
        }
        replace_suit = {
            'spades': 1,
            'hearts': 2,
            'clubs': 3,
            'diamonds': 4
        }

        # 重定义小于:<
        if self.value == other.value:
            if replace_suit[self.suit] > replace_suit[other.suit]:
                return True
            else:
                return False
        else:
            if replace_value[self.value] > replace_value[other.value]:
                return False
            else:
                return True

    def __gt__(self, other):
        # 重定义大于:>
        if self < other:
            return False
        else:
            return True


card1 = Card('2', 'spades')
card2 = Card('2', 'hearts')
card3 = Card('2', 'clubs')
card4 = Card('2', 'diamonds')
card5 = Card('J', 'diamonds')
print(card1 > card2)
print(card2 > card3)
print(card4 > card3)
print(card1 > card5)
print(card1 < card2)


