from functools import reduce


def get_sum_use_python(l):
    return sum(l)

def f(m, n):
    return m + n

def get_sum_use_reduce(l):
    return reduce(f, l)

def get_sum_use_lambda(l):
    return reduce(lambda m, n: m + n,l)

if __name__ == "__main__":
    l = [1, 2, 3, 5, 7]
    print(get_sum_use_python(l))
    print('------------------')
    print(get_sum_use_reduce(l))
    print('+++++++++++++++++++')
    print(get_sum_use_lambda(l))