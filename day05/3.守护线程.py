"""
@author Chr.yl
    守护线程,设置为守护线程的子线程在主线程挂掉之后,也会挂掉
    子线程守护主线程
"""

import time
import threading


def song():
    for i in range(5):
        print('song....')
        time.sleep(0.5)


if __name__ == '__main__':
    for i in range(5):
        # 线程方式
        # threading.Thread(target=函数名)
        thread_song = threading.Thread(target=song)
        # 子线程守护主线程: true为守护主线程
        thread_song.setDaemon(True)
        # 2 字典传递方式
        thread_song.start()
        print('GameOver..')
        # 程序退出,默认无效,要设置守护线程,根子线程约定
        exit()
