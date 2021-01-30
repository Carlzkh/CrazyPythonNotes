"""
10. 定义 fn(n）函数，其中 n表示输入 n行n列的矩阵（数的方阵〉 在输出时，先输出
列的矩阵，再输出该矩阵的转置形式 例如，当参数为 时，先输出matrix：
123
456
789
再输出Transposed matrix：
147
258
369
"""


def fn(n):
    list_init = list(range(1, n*n+1))
    # print(list_init)
    for i in range(n):
        for j in range(n):
            print(list_init[j], end='')
        for k in range(n):
            list_init.remove(list_init[0])
        print()


fn(3)
