"""在使用 raise 语句时可以不带参数，此时 raise 语句处于 except 块中，它将
会自动引发当前上下文激活的异常 否则，通常默认引发 RuntimeError 异常
"""
class AuctionException(Exception):
    pass


class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            # 此处只是简单地打印异常信息
            print('转换出异常:', e)
            # 再次引发自定义异常
            raise
            # raise AuctionException('竞拍价必须是数值，不能包含其他字符！')   # ①
        if self.init_price > d:
            raise AuctionException('竞拍价比起拍价低，不允许竞拍 ！')
        # initPrice = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid('u')
    except AuctionException as ae:
        # 再次捕获到 bid （）方法中的异常，并对该异常进行处理
        print('main 函数捕获的异常：', ae)


main()
