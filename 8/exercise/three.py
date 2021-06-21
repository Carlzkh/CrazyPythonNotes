"""
3. 自定义 个迭代器，该迭代器分别返回 1+2, 1+2+3 …的累积和

"""


class Accumulation:
    def __init__(self):
        self.first = 1
        self.second = 2

    def __next__(self):
        acc1 = self.first + self.second
        self.first, self.second = acc1, self.second + 1
        return acc1

    def __iter__(self):
        return self


acc = Accumulation()
print(next(acc))
for i in range(10):
    print(next(acc))
