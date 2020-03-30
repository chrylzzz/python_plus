"""
@author Chr.yl
    Lock:互斥锁,多个对象只加一把锁即可,我用了你用不了,你用了我不用的概念,就是多个对象共用同一把锁,你得等我用完了在用
    acquire 上锁
    release 解锁
"""
import threading
import time

num = 0


# work1
def work1():
    global num
    # 访问资源,尽可能锁少的资源,但是要兼顾效率
    # 上锁
    lock.acquire()
    for i in range(5000000):
        num += 1
    lock.release()
    print('work1:', num)


# work2
def work2():
    global num
    # 互斥锁生效,
    lock.acquire()
    for i in range(5000000):
        num += 1
    lock.release()
    print('work2:', num)


if __name__ == '__main__':
    # 互斥锁
    lock = threading.Lock()

    thread_work1 = threading.Thread(target=work1)
    thread_work2 = threading.Thread(target=work2)

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    thread_work1.start()
    thread_work2.start()
