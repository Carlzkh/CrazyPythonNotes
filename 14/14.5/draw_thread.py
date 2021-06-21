import threading
import time
import account


def draw(account1, draw_awount):
    if account1.balance >= draw_awount:
        print(threading.current_thread().name + "取钱成功：" + str(draw_awount))
        # time.sleep(0.001)
        account1.balance -= draw_awount
        print("\t余额为：" + str(account1.balance))
    else:
        print(threading.current_thread().name + "取钱失败,余额不足")


while True:
    acct = account.Account("1234567", 1000)
    threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
    threading.Thread(name='乙', target=draw, args=(acct, 800)).start()
