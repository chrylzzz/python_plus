"""
@author Chr.yl
    线程类
"""
import threading
import time


# 继承Thread
class MyThread(threading.Thread):

    def __init__(self, num):
        # 重写init  先调用父类的init
        super().__init__()
        self.num = num

    # 重写 父类 的run方法
    def run(self):
        for i in range(5):
            print('ing...:', i, self.name, self.num)
            time.sleep(0.5)


if __name__ == '__main__':
    # init 修改之后,必须修改构造方法
    my_thread = MyThread(10)
    # my_thread.run()
    my_thread.start()
