import threading


def action(max1):
    for i in range(max1):
        print(threading.current_thread().name + " action " + str(i))


threading.Thread(target=action, args=(100,), name='新线程').start()
for j in range(100):
    if j == 20:
        jt = threading.Thread(target=action, args=(100,), name="被Join的线程")
        jt.start()
        jt.join()
    print(threading.current_thread().name + " " + str(j))
