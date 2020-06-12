import datetime
import random


def write_file():
    """写入文件"""
    file_name = "write_test.txt"
    f = open(file_name, 'w', encoding='utf-8')
    f.write('春眠不觉晓，')
    f.write('处处闻帝鸟。')
    f.write('夜来风雨声，')
    f.write('花落知多少。')

    f.close()

def write_multi_line():
    file_name = "write_multi_line.txt"
    with open('file_name', 'w', encoding='utf-8') as f:
        list = ['第一行', '第二行', '第三行']
        f.writelines(list)

def write_user_log():
    rest = '用户 {0} - 访问时间 {1}'.format(random.randint(1000, 9999), datetime.datetime.now())
    file_name = 'write_user_log.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(rest)
        f.write('\n')

def write_read_write():
    file_name = 'write_test.txt'
    with open(file_name, 'r+', encoding='utf-8') as f:
        read_content = f.read()
        if '0' in read_content:
            f.write('00000000000')
        else:
            f.write('else,else,else,else,else,else,else,else,else,else,else')

if __name__ == '__main__':
    # write_file()
    # write_multi_line()
    # write_user_log()
    write_read_write()