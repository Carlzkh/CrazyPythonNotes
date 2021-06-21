"""
如果需要在程序中自行引发异常，则应使用 raise 吾句 raise 语句有如下 种常用的用法
ra ise 单独 raise 该语句引发当前上下文中捕获的异常 比如在 except 块中），或默
认引发 RuntimeError 异常
);>- raise 异常类： raise 后带 个异常类 吾句引发指定异常类的默认实例
);>- raise 异常对象：引 定的异常对象
上面 种用法最终都是要引发 个异常实例（ 即使指定的是异常类 实际上也是引 发该类的默
认实例） , raise 吾句每次只能引发 个异常实例
"""


# 自定义异常类
class AuctionException(Exception):
    pass


def main():
    try:
        # 使用 try . . . except 来捕获异常
        # 此时即使程序出现异常 也不会传播给 main 函数
        mtd(3)
    except Exception as e:
        print('程序出现异常：', e)
    # 不使用 try ... except 捕获异常，异常会传播出来导致程序中止
    mtd(3)


def mtd(a):
    if a > 0:
        raise AuctionException('a的值大于0，不符合要求')


main()

