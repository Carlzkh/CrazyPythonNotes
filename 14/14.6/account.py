import threading


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        self._flag = False

    def get_balance(self):
        return self._balance

    def draw(self, draw_amount):
        self.cond.acquire()
        try:
            if not self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name + "取钱成功，取出金额：" + str(draw_amount))
                self._balance -= draw_amount
                print("\t余额为：" + str(self._balance))
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        finally:
            self.cond.release()

    def deposit(self, deposit_amount):
        self.cond.acquire()
        try:
            if self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name + "存钱成功，存入金额：" + str(deposit_amount))
                self._balance += deposit_amount
                print("\t余额为：" + str(self._balance))
                self._flag = True
                # 唤醒其他线程
                self.cond.notify_all()
        finally:
            self.cond.release()

