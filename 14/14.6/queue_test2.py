import threading
import time
import queue


def product(bq):
    str_tuple = ("python", "kotlin", "swift")
    for i in range(99999):
        print(threading.current_thread().name + "生产者准备生产元组元素！")
        time.sleep(0.2)
        bq.put(str_tuple[i % 3])
        print(threading.current_thread().name + "生产者生产元组元素完成！")


def consume(bq):
    while True:
        print(threading.current_thread().name + "消费者准备消费元组元素！")
        time.sleep(0.2)
        t = bq.get()
        print(threading.current_thread().name + "消费者消费【%s】元素完成！" % t)


bq1 = queue.Queue(maxsize=1)

threading.Thread(target=product, args=(bq1,)).start()
threading.Thread(target=product, args=(bq1,)).start()
threading.Thread(target=product, args=(bq1,)).start()

threading.Thread(target=consume, args=(bq1,)).start()
