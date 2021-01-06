"""
3. 用户输入 一个整数 n ，生成长度为 n的列表，将 n个随机数放入列表中
"""
import random
N = int(input("输入整数N："))
list1 = []
for i in range(N):
    list1.append(random.randint(0, 100))
print(list1)
