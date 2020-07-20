def pow():
    return (x * x for x in [1, 2, 3, 4,5])

def pow2():
    for i in [1, 2, 3, 4, 5]:
        yield i * i

if __name__ == '__main__':
    aa = pow()
    print(aa.__next__())
    print(aa.__next__())
    print(aa.__next__())
    bb = pow2()
    print(next(bb))
    print(next(bb))
    print(next(bb))
    print(next(bb))
    print(next(bb))