"""
@author Chr.yl
    线程类
"""
import threading
import time


class MyThread(threading.Thread):
    # 重写 父类 的run方法
    def run(self):
        for i in range(5):
            print('ing...:', i)
            time.sleep(0.5)


if __name__ == '__main__':
    my_thread = MyThread()
    # my_thread.run()
    my_thread.start()
