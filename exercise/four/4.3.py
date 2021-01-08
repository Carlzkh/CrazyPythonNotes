"""
3. 给定奇数 输出（横、坚、斜的总和相等）
08 O1 06
03 05 07
04 09 02
给定奇数 输出（横、坚、斜的总和相等）
17 24 O1 08 15
23 05 07 14 16
04 06 13 20 22
10 12 19 21 03
11 18 25 02 09
依此类推。

"""
n = int(input("输入一个奇数："))
list1 = []
for i in range(1, n * n + 1):
    list1.append(i)
x = 0
y = n
for i in range(n):
    for j in range(x, y):
        print(list1[j] + ' ', end='')
    x += n
    if y + n <= n*n:
        y += n

    print()












