from concurrent.futures import ThreadPoolExecutor
import threading
import time


def action(thread_max):
    my_sum = 0
    for i in range(thread_max):
        print(threading.current_thread().name + ' ' + str(i))
        my_sum += 1
    return my_sum


# 创建一个包含两个线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 像线程池中提交一个任务，50是action函数的参数
future1 = pool.submit(action, 50)
future2 = pool.submit(action, 100)
print(future1.done())
time.sleep(3)
print(future2.done())
print(future1.result())
print(future2.result())
pool.shutdown()
