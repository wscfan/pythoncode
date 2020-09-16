import threading
import time
import threading


class LoopThread(threading.Thread):
    n = 0
    def run(self):
        while self.n < 5:
            print(self.n)
            now_threading = threading.current_thread()
            print('loop_thread: {0}'.format(now_threading.name))
            time.sleep(1)
            self.n += 1

if __name__ == '__main__':
    now_thread = threading.current_thread()
    print('now_thread: {0}'.format(now_thread.name))
    t = LoopThread(name='loop_thread_oop')
    t.start()
    t.join()