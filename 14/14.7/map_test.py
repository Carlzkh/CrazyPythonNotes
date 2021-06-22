from concurrent.futures import ThreadPoolExecutor
import threading
import time


def action(thread_max):
    my_sum = 0
    for i in range(thread_max):
        print(threading.current_thread().name + ' ' + str(i))
        my_sum += 1
    return my_sum


with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, (50, 100, 150))
    print('-------------------')
    for j in results:
        print(j)
