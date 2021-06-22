import threading
import time


class Account:
    def __init__(self, account_no, _balance):
        self.account_no = account_no
        self._balance = _balance
        self.lock = threading.RLock()

    def get_balance(self):
        return self._balance

    def draw(self, draw_amount):
        self.lock.acquire()
        try:
            if self._balance >= draw_amount:
                print(threading.current_thread().name + "取钱成功，取出金额：" + str(draw_amount))

                self._balance -= draw_amount
                print("\t余额为：" + str(self._balance))
            else:
                time.sleep(0.1)
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            self.lock.release()

