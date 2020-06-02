def use_filter(l):
    rest = filter(lambda n: n % 2 != 0, l)
    return rest

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11]
    rest = use_filter(l)
    print(list(rest))