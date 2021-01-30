"""
5. 定义 fn(n)函数，该函数返回1~n 的立方和，即求 1+2*2*2叮叮叮＋… 句句
"""


def fn(n):
    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i*i*i
    return sum_of_cubes


sum1 = fn(1)
sum2 = fn(2)
sum3 = fn(3)
print(sum1, sum2, sum3)
