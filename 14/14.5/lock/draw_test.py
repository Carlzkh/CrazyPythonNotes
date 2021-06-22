import threading
import Account


def draw(account, draw_amount):
    account.draw(draw_amount)


while True:
    acct = Account.Account("1234567", 1000)
    threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
    threading.Thread(name='乙', target=draw, args=(acct, 800)).start()
