"""
@author Chr.yl

"""
import multiprocessing
import time


def work1():
    for i in range(10):
        print("zzzz..")
        time.sleep(0.5)


if __name__ == '__main__':
    process = multiprocessing.Process(target=work1)
    process.start()
