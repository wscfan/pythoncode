def pow_number(l):
    """
    根据给定的列表数据，计算里边每一项的立方
    :param l: int 类型的列表或者元组
    :return: 原来列表中每一项的立方
    """
    rest_list = []
    for x in l:
        rest_list.append(x * x * x)
    return rest_list

def f(n):
    return n * n * n

def pow_number_use_map(l):
    """
    使用 map 函数计算给定列表的每一项的立方
    :param l: int 类型的列表或者元组
    :return: 原来列表中每一项的立方
    """
    return map(f, l)

def pow_number_use_lambda(l):
    """
    使用 map 函数计算 lambda 表达式计算给定列表的每一项的立方
    :param l: int 类型的列表或者元组
    :return: 原来列表中每一项的立方
    """
    return map(lambda n: n * n * n, l)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    rest = pow_number(l)
    print(rest)

    print('---------------')

    rest_map = pow_number_use_map(l)
    print(list(rest_map))

    print('----------------')

    rest_lambda = pow_number_use_lambda(l)
    print(list(rest_lambda))
