import threading
import queue

bq = queue.Queue(1)
lock = threading.RLock()


def action1(bq):
    for i in range(1, 53, 2):
        bq.put(i)
        print(i, end='')
        print(i + 1, end='')


def action2(bq):
    for i in range(26):
        bq.get()
        print(chr(65 + i), end='')


# 创建并启动第一个线程
t1 = threading.Thread(target=action1, args=(bq, ))
t1.start()
# 创建并启动第二个线程
t2 = threading.Thread(target=action2, args=(bq, ))
t2.start()
