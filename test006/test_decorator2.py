def log(func):
    def wrapper():
        print('开始执行。。。')
        func()
        print('结束执行。。。')
    return wrapper

@log
def hello():
    print("hello world ！")

if __name__ == '__main__':
    hello()