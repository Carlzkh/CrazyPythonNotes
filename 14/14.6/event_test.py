import threading
import time

event = threading.Event()


def cal(name):
    print('%s启动' % threading.current_thread().getName())
    print('%s准备开始计算状态' % name)
    event.wait()
    print('%s收到通知' % threading.current_thread().getName())
    print('%s正式开始计算' % name)


threading.Thread(target=cal, args=('甲',)).start()
threading.Thread(target=cal, args=('乙',)).start()
time.sleep(2)
print('----------------------')
print('主线程发出事件')
event.set()
