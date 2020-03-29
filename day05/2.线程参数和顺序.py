"""
@author Chr.yl
    线程中传递参数的三种方法:
        1.元组
        2.字典
        3.混合使用元组和字典 :注意,元组只传一个数据时需要有,

"""
import time
import threading


def sing(a, b, c):
    print("参数:", a, b, c)
    print('sing')
    time.sleep(0.5)


def song():
    print('song')
    time.sleep(0.5)


if __name__ == '__main__':
    for i in range(5):
        # 线程方式
        # threading.Thread(target=函数名)
        thread_song = threading.Thread(target=song)
        # 线程传递参数
        # 1 元组传递
        # thread_sing = threading.Thread(target=sing, args=(100, 100, 100))
        # 2 字典传递方式
        # thread_sing = threading.Thread(target=sing, kwargs={'b': 100, 'c': 100, 'a': 100})
        # 3 混合使用元组和字典 ,注意,元组只传一个数据时需要有,
        thread_sing = threading.Thread(target=sing,
                                       args=(10,),
                                       kwargs={'b': 100, 'c': 100})
        # 启动
        thread_song.start()
        thread_sing.start()
