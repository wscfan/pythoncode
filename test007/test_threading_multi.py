import threading

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    print("--------------->{0}".format(n))

class changeBalanceThread(threading.Thread):
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        for i in range(1000):
            change_it(self.num)

if __name__ == "__main__":
    t1 = changeBalanceThread(5)
    t2 = changeBalanceThread(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("this last {0}".format(balance))