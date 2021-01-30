"""
4. 自定义 1个生成器，该生成器可按顺序返回 52 张扑克牌 分别是黑桃、红心、草花、方块的2~A
spades：黑桃♠， hearts：红桃♥， clubs：梅花♣， diamonds：方片♦
"""
colors = 'spades hearts clubs diamonds'.split(' ')
values = [str(n) for n in range(2, 11)] + list('JQKA')


def playing_cards():
    for i in range(4):
        for j in range(13):
            card_next = colors[i]+values[j]
            yield card_next


card_ = playing_cards()
print(list(card_))  # 可用list()或tuple()将生成器能生成的所有值转换成列表或元组，也可用如下的循环输出。
# for k in range(52):
#     print(next(card_))
