class ApiException(Exception):
    """  我的自定义异常 """
    err_code = ''
    err_msg = ''
    def __init__(self, err_code=None, err_msg=None):
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return 'Error: {0} - {1}'.format(self.err_code, self.err_msg)

class BadParamsException(ApiException):
    err_code = '40005'
    err_msg = '不合法的调用凭证'

def devide(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise BadParamsException()
    if num2 == 0:
        raise ApiException('40002', '除数不能为0')
    return num1 / num2

if __name__ == '__main__':
    try:
        rest = devide(5, 's')
    except ApiException as err:
        print('出错了')
        print(err)