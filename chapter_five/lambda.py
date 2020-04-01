"""
lambda表达式就是匿名的单行函数体的函数
"""
'''
lambda不需要定义函数，是代码更简洁（单行函数）
对于复用次数不多的函数，lambda可以及时释放，性能更优
'''
x = map(lambda x: x * x, range(8))
print([i for i in x])


























