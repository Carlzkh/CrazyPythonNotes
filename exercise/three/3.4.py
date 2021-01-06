"""
4. 用户输入 一个整数 n，生成长度为 n的列表，将 n个随机的奇数放入列表中
"""
import random
N = int(input("输入整数N："))
list1 = []
for i in range(N):
    n = random.randint(0, 100)
    if n % 2 != 0:
        list1.append(n)
    else:
        list1.append(n+1)
print(list1)
