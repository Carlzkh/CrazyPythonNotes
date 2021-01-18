"""
3. 自定义 1个迭代器，该迭代器分别返回 1+2, 1+2+3 …的累积和
"""


class CumulativeSum:
    def __init__(self):
        self.first = 1
        self.second = 2
        self.cumulative_sum = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.cumulative_sum, self.second = self.cumulative_sum+self.second, self.second+1
        return self.cumulative_sum


cumulative_sum = CumulativeSum()
print(next(cumulative_sum))
print(next(cumulative_sum))
print(next(cumulative_sum))
for i in cumulative_sum:
    if i <= 100:
        print(i)
    else:
        break
