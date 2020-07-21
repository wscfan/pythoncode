class InterRange(object):

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self

class GenRange(object):
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def get_num(self):
        while True:
            self.start += 1
            if self.start >= self.end:
                break
            yield self.start

if __name__ == '__main__':
    # iter = InterRange(5, 10)
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))

    gen = GenRange(5, 10).get_num()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))