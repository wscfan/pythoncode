from datetime import datetime
import random
def gen_trans_id(date = None):
    """
    根据所传入的时间得到一个唯一的交易流水id
    :param date: 日期
    :return: 交易流水字符串
    """
    # 如果没有传入时间，则使用系统当前的时间
    if date == None:
        date = datetime.now()
    # 日期 + 时间 + 毫秒 + 6位随机数
    # return date.strftime('%Y%m%d%H%M%S%f') + str(random.randint(100000, 999999))
    return '{0}{1}'.format(date.strftime('%Y%m%d%H%M%S%f'), random.randint(100000, 999999))