"""
8. 自定义代表 克牌的 Card 类（包括花色和牌面值），为 Card 类提供自定义的比较大小的运
算符支持 大小比较标准是先比较牌面值，如果牌面值相等则比较花色，花色大小规则为 黑桃＞红桃
＞草花＞方块

"""


class Card:
    def __init__(self, poker_suit, face_value):
        self.poker_suit = poker_suit
        self.face_value = face_value

    def __gt__(self, other):
        # 要求参与“〉”比较的另 个操作数必须是 Rectangle
        if not isinstance(other, Card):
            raise TypeError('比较要求目标是Rectangle')
        if self.face_value > other.face_value:
            return True
        elif self.face_value == other.face_value:
            if self.poker_suit == '黑桃':
                return True
            elif self.poker_suit == '红桃' and other.poker_suit != '黑桃':
                return True
            elif self.poker_suit == '梅花' and (other.poker_suit == '方片' or other.poker_suit == '梅花'):
                return True
            elif self.poker_suit == '方片' and other.poker_suit == '方片':
                return True
        else:
            return False


r1 = Card('黑桃', 4)
r2 = Card('方片', 5)
print(r1 > r2)  # True
print(r1 < r2)  # True


# 参考答案
flowers = ('♦', '♣', '♥', '♠')
values = ('2', '3', '4', '5',
          '6', '7', '8', '9',
          '10', 'J', 'Q', 'K', 'A')


class Card(object):
    def __init__(self, flower, value):
        self.flower = flower
        self.value = value

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError('+运算要求目标是Card')
        if values.index(self.value) > values.index(other.value):
            return True
        elif values.index(self.value) == values.index(other.value) and \
                flowers.index(self.flower) > flowers.index(other.flower):
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError('+运算要求目标是Card')
        if values.index(self.value) == values.index(other.value) and \
                flowers.index(self.flower) == flowers.index(other.flower):
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, Card):
            raise TypeError('+运算要求目标是Card')
        return self > other or self == other

    def __repr__(self):
        return '%s-%s' % (self.flower, self.value)


if __name__ == "__main__":
    cd1 = Card(flower="♠", value="A")
    cd2 = Card(flower="♠", value="K")
    cd3 = Card(flower="♥", value="K")
    cd4 = Card(flower="♥", value="J")
    cd5 = Card(flower="♥", value="K")
    print(cd1 > cd2)  # True
    print(cd1 < cd2)  # False
    print(cd2 < cd3)  # False
    print(cd2 > cd3)  # True
    print(cd3 == cd5)  # True
    print(cd3 < cd5)  # False
    print(cd3 > cd5)  # False
    print(cd3 >= cd5)  # True
    print(cd3 <= cd5)  # True
