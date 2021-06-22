from concurrent.futures import ThreadPoolExecutor
import threading
import time


def action(thread_max):
    my_sum = 0
    for i in range(thread_max):
        print(threading.current_thread().name + ' ' + str(i))
        my_sum += 1
    return my_sum


with ThreadPoolExecutor(max_workers=2) as pool:
    future1 = pool.submit(action, 50)
    future2 = pool.submit(action, 100)

    def get_result(future):
        print(future.result())

    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    print('----------------------')
