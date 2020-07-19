
class PowNumber(object):
    """
    迭代器
    生成1,2,3,...的平方
    """
    num = 0
    def __next__(self):
        self.num += 1
        if self.num > 10:
            raise StopIteration
        return self.num * self.num

    def __iter__(self):
        return self

if __name__ == '__main__':
    pow = PowNumber()
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    print(next(pow))
    print(next(pow))
    print(next(pow))
    print(next(pow))
    print(next(pow))
    for i in pow:
        print(i)