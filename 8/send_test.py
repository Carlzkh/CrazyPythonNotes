"""
需要说明的是，只有等到生成器被“冻结”之后，外部程序才能使用 send()方法向生成器发送数据。
获取生成器第一次所生成的值，应该使用 next()函数；
如果程序非要使用 send()方法获取生成器第一次所生成的值，也不能向生成器发送数据，只能为该方法传入 None 参数

"""


def square_gen(val):
    i = 0
    out_val = None
    while True:
        # 使用yield语句生成值，使用out_val接收 send()方法发送的参数值
        out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
        # 如果程序使用 send()方法获取下一个值，out_val会获取 send()方法的参数值
        if out_val is not None:
            print('＝＝＝＝%d' % out_val)
        i += 1


sg = square_gen(5)
# 第一次调用send()方法获取值，只能传入None作为参数
print(sg.send(None))
print(next(sg))
print('----------------')
# 调用 send （）方法获取生成器的下一个值，参数 会被发送给生成器
print(sg.send(9))
# 再次调用 next （） 函数获取生成器的下 个值
print(next(sg))


'''
> close（）： 用于关闭生成器
> throw（）： 该方法用于在生成器内部（ yield 语句内）引发一个异常
'''
# sg.throw(ValueError)  # 让生成器引发异常
sg.close()
print(next(sg))  # StopIteration
