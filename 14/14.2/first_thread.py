import threading
# 定义 个普通的 action 方法，该方法准备作为线程执行体


def action(max1):
    for m in range(max1):
        # 调用 threadi 呵棋块的 cur re 口 t thread （）函数获取当前线程
        # 调用线程对象的 getName （）方法获取当前线程的名字
        print(threading.current_thread().getName() + "_action_" + str(m))


# 下面是主程序(也就是主线程的线程执行体)
for i in range(100):
    # 调用 threading 模块的 current_thread （）函数获取当前线程
    print(threading.current_thread().getName() + "" + str(i))
    if i == 20:
        # 创建并启动第一个线程
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        # 创建并启动第2个线程
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
print('主线程执行完成!')
