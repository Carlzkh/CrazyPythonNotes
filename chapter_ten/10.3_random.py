import random

# print(random.seed(a='None', version=2))  # random.seed 有参数时，下面的随机函数，生成的随机数都是不变的了！！！！
# 不执行random.seed，或random.seed()不带参数，下面的随机数还是正常的随机！
print(random.randrange(start=1, stop=77, step=3))
print(random.randrange(1, 77, 3))
print(random.randint(1, 4))  # 1-4之间的整数，包含1和4
print(random.choice('anyway'))  # 随机取一个，参数不能为空，空序列(空列表.....)
print(random.choices(['apple', 'pink', 'orange'], weights=[5, 5, 1], k=6))  # 按权重取k个元素
list1 = ['apple', 'pink', 'orange', 'pink', 'orange', 'orange', 'orange']
print(random.shuffle(list1))  # 洗牌
print(list1)
print(random.sample(list1, 4))  # 随机取k个，不会重复取！！k超过序列长度就会报错。choices()会重复取！
print(random.random())  # 0-1之间的浮点数，包含0.0，不包含1.0
print(random.uniform(1, 4))  # 1-4之间的浮点数，包含1和4
print(random.expovariate(-2))  # 成指数分布的随机数




