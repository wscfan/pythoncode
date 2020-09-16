import threading
import time

def loop():
    """新线程执行的代码"""
    n = 0
    while n < 5:
        print(n)
        now_thread = threading.current_thread()
        print('loop : {0}'.format(now_thread.name))
        time.sleep(1)
        n += 1

def use_thread():
    """使用线程来实现"""
    # 当前正在执行的线程名称
    now_thread = threading.current_thread()
    print(now_thread.name)
    # 设置线程
    t = threading.Thread(target=loop, name='loop_thread')
    # 启动线程
    t.start()
    # 挂起线程
    t.join()

if __name__ == '__main__':
    use_thread()