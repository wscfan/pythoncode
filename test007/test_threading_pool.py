import time
import threading
from multiprocessing.dummy import Pool


def run(n):
    time.sleep(2)
    print(threading.current_thread().name, n)

def main():
    """使用传统方法来做任务"""
    t1 = time.time()
    for n in range(2):
        run(n)
    print(time.time() - t1)

def main_use_pool():
    """使用线程池优化"""
    t1 = time.time()
    n_list = range(20)
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    print(time.time() - t1)

if __name__ == '__main__':
    main_use_pool()