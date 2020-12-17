import os
import time
from multiprocessing import Process


def do_sth(name):
    """进程需要做的事情"""
    print("进程名称：{0},pid：{1}".format(name, os.getpid()))
    time.sleep(5)
    print("进程需要做的事情")

if __name__ == '__main__':
    p = Process(target=do_sth, args=('my process', ))
    # 启动进程
    p.start()
    # 挂起进程
    p.join()