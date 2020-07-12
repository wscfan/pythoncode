def hello():
    """简单功能模拟"""
    print("hello world")

def hello_wrapper():
    print('开始执行 hello')
    hello()
    print('结束执行 hello')

if __name__ == '__main__':
    hello_wrapper()