"""

yield cur 语句 的作用有两点。
〉每次返回一个值，有点类似于 return 语句
》冻结执行，程序每次执行到 yield 语句时就会被暂停
在程序被 yield 语句冻结之后，当程序再次调用 next（） 函数获取生成器的下一个值 ，程序才
会继续向下执行
需要指出 的是，调用包 yield 语句的函数并不会立即执行，它只是返回一个生成器。只有当
程序通过 next （） 函数调用生成器或遍历生成器时，函数才会真正执行
"""


def test(val, step):
    print('一一一－函数开始执行一－ －－')
    cur = 0
    # 遍历 val
    for i in range(val):
        # cur 添加 i*step
        cur += i * step
        yield cur


# 执行函数，返回生成器
t = test(10, 2)
print('=================')
# 获取生成器的第一个值
print(next(t))  # ，生成器被“冻结”在 yield
print(next(t))  # ，生成器被再次“冻结”在 yield

for ele in t:
    print(ele, end=' ')


# 再次创建生成器
t = test(10, 1)
# 将生成器转换成列表
print(list(t))
# 再次创建生成器
t = test(10, 3)
# 将生成器转换成元组
print(tuple(t))
