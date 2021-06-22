import threading


def print_increasing_number():
    for i in range(1, 76):
        print(threading.current_thread().name + ':' + str(i))


t1 = threading.Thread(name='线程1', target=print_increasing_number).start()
t2 = threading.Thread(name='线程2', target=print_increasing_number).start()
t3 = threading.Thread(name='线程3', target=print_increasing_number).start()
