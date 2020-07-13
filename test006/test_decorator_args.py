from functools import wraps


def log(name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('{0}start.......'.format(name))
            func(*args, **kwargs)
            print('{0}end.......'.format(name))
        return wrapper
    return decorator

@log('张三')
def test(a, b, *args, **kwargs):
    """哈哈哈哈哈"""
    print(a * b)
    print(args)
    print(kwargs)

if __name__ == '__main__':
    print(test.__name__)
    print(test.__doc__)
    test(12, 23, 34, 34, 56, 99, aa='123', bb=123)