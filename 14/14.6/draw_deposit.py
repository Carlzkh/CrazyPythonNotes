import threading
import account


# 定义 个函数，模拟重复 max 次执行取钱操作
def draw_many(account1, draw_amount, max1):
    for i in range(max1):
        account1.draw(draw_amount)


# 定义一个函数，模拟重复 max 次执行存款操作
def deposit_many(account2, deposit_amount, max2):
    for i in range(max2):
        account2.deposit(deposit_amount)


# 创建 个账户
acct = account.Account('1234567', 0)
# 创建并启动 个“取钱”线程
threading.Thread(name='取钱者', target=draw_many, args=(acct, 800, 100)).start()
# 创建并启动一个“存款”线程
threading.Thread(name='存款者甲', target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name='存款者乙', target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name='存款者丙', target=deposit_many, args=(acct, 800, 100)).start()
