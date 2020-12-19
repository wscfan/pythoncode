def count_down(n):
    while n > 0:
        yield n
        n -= 1

def yield_test():
    while True:
        n = (yield )
        print(n)

if __name__ == '__main__':
    # rest = count_down(5)
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    rest = yield_test()
    next(rest)
    rest.send('66666')
    rest.send('77777')