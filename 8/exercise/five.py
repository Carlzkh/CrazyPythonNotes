"""
5. 定义 个生成器，可依次返回 2, 3, …的阶乘

"""


def test(val, step):
    print('一一一－函数开始执行一－ －－')
    cur = 1
    # 遍历 val
    for i in range(2, val):
        # cur 添加 i*step
        cur *= i * step
        yield cur


print(list(test(10, 1)))


# 参考答案
def factorial_generator(n):
    rvt_list = [1]
    for i in range(2, n + 1):
        rvt_list.append(rvt_list[-1] * i)
    print('------------', len(rvt_list))
    for i in range(n):
        yield rvt_list[i]


if __name__ == '__main__':
    fg = factorial_generator(10)
    print(next(fg))  # 1，生成器“冻结”在yield处
    print(next(fg))  # 2，生成器再次“冻结”在yield处
    for ele in fg:
        print(ele, end=' ')