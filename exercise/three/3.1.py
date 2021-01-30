"""
1. 提示用户输入 N个字符串 ，将它们封装成元组，然后计算并输入该元组乘以3的结果，
再计算并输出该元组加上（ 'fkjava'，'crazyit'）的结果
"""
list1 = []
N = int(input("输入多少个元素？"))
for i in range(N):
    element = input("输入%d个字符串，第%d个" % (N, (i+1)))
    list1.append(element)

tuple1 = tuple(list1)
tuple2 = tuple1 * 3
print("元组乘以3：", tuple2)
tuple3 = tuple1 + ('fkjava', 'crazyit')
print("元组加元组：", tuple3)
