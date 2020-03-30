"""
@author Chr.yl
    global 可以多线程共享变量
"""
import threading
import time

num = 0


# work1
def work1():
    global num
    for i in range(5):
        num += 1
    print('work1:', num)


# work2
def work2():
    print('work2:', num)


if __name__ == '__main__':
    thread_work1 = threading.Thread(target=work1)
    thread_work2 = threading.Thread(target=work2)

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    thread_work1.start()
    thread_work2.start()
