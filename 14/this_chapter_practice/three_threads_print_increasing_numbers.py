import threading
from concurrent.futures import ThreadPoolExecutor


class PrintIncreasingNumber:
    def __init__(self):
        self.print_no = 0
        self.cond = threading.Condition()
        self.state = 1

    def print_increasing_number(self, thread_no):
        try:
            self.cond.acquire()
            while self.state != thread_no:
                self.cond.wait()
            # 打印5个连续数值
            for k in range(5):
                self.print_no += 1
                print("thread%d : %d" % (thread_no, self.print_no))
            # 每打印5个数字，state加1，控制轮到下一个线程来执行打印
            self.state = self.state % 3 + 1
            self.cond.notify_all()
        finally:
            self.cond.release()


def action(print_user, thread_no):
    for j in range(5):
        print_user.print_increasing_number(thread_no)


user = PrintIncreasingNumber()

'''
t1 = threading.Thread(name='线程1', target=action, args=(user, 1)).start()
t2 = threading.Thread(name='线程2', target=action, args=(user, 2)).start()
t3 = threading.Thread(name='线程3', target=action, args=(user, 3)).start()
这种方法与下面的方法效果一样！
'''
with ThreadPoolExecutor(max_workers=3) as pool:
    # 启动3条线程
    for i in range(3):
        # 使用线程池启动3条线程
        pool.submit(action, user, i + 1)
