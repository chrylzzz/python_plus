"""
@author Chr.yl
    主线程会等待子线程执行完再结束
    只有str才能 + 连接 : print('线程数量:' + str(thread_list))
    否则用 : print('线程数量:', thread_list)
"""
import time
import threading


def sayStory():
    print('sorry')
    time.sleep(0.5)


if __name__ == '__main__':
    for i in range(5):
        # 线程方式
        # threading.Thread(target=函数名)
        thread_obj = threading.Thread(target=sayStory)
        # 查看正在活跃的线程的名称,和数量
        thread_list = threading.enumerate()
        # print('线程数量:' + str(thread_list) + '\n,线程数量:' + str(len(thread_list)))
        print('线程数量:', thread_list)
        # 名称 ,当前线程对象
        this_thread = threading.current_thread()
        print("当前线程对象:", this_thread)
        # 启动
        thread_obj.start()
        # 单线程
        # sayStory()

# 线程方式
