import threading


def action(max1):
    for i in range(max1):
        print(threading.current_thread().name + " action " + str(i))


t = threading.Thread(target=action, args=(100,), name='后台线程')
t.daemon = True
t.start()
for j in range(10):
    print(threading.current_thread().name + " " + str(j))
