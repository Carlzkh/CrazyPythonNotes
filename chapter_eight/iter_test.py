"""
如果开发者需要实现法代器，只要实现如下两个方法即可
>__iter__(self) 该方法返回一个法代器(iterator)，迭代器必须包含next()方法，
该方法返回迭代器的下一个元素。
>__reversed__(self),该方法主要为内建的 reversed()反转函数提供支持，
当程序调用 reversed()函数对指定迭代器执行反转时，实际上是由该方法实现的

下面程序实现一个斐波那契数列的迭代器
"""
# 定义 个代表斐波那契数列的迭代器


class Fibs:
    def __init__(self, _len):
        self.first = 0
        self.sec = 1
        self._len = _len
    # 定义法代器所需的＿next一一方法

    def __next__(self):
        # 如果 len 属性为 ，结束法代
        if self._len == 0:
            raise StopIteration('长度为0，结束迭代')
        # 完成数列计算
        self.first, self.sec = self.sec, self.first + self.sec
        # 数列长度减
        self._len -= 1
        return self.first
    # 定义 iter 方法 该方法返回迭代器

    def __iter__(self):
        return self
# Fibs 对象


fibs = Fibs(10)
# 获取法代器的下一个元素
print(next(fibs))
# 使用 for 循环遍历法代器
for el in fibs:
    print(el, end=' ')


# 将列表转换为法代器
my_iter = iter([2, 'one', 4])
# 依次获取法代器的下一个元素
print(my_iter.__next__())  # 2
print(my_iter.__next__())  # one
