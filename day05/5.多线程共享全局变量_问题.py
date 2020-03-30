"""
@author Chr.yl
    global 可以多线程共享变量,但是存在问题,当多个线程访问同一个资源,存在资源竞争,优先让一个先执行
"""
import threading
import time

num = 0


# work1
def work1():
    global num
    for i in range(5000000):
        num += 1
    print('work1:', num)


# work2
def work2():
    global num
    for i in range(5000000):
        num += 1
    print('work2:', num)


if __name__ == '__main__':
    thread_work1 = threading.Thread(target=work1)
    thread_work2 = threading.Thread(target=work2)

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    thread_work1.start()
    # join 让某个线程优先执行,执行完之后其他才能执行
    thread_work1.join()
    thread_work2.start()
