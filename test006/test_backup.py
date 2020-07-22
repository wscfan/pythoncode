import os
import os.path

class FileBackup(object):
    """
    文本文件备份
    """
    def __init__(self, src, dist):
        """
        构造方法
        :param src: 需要备份的文件目录
        :param dist: 备份后的目录
        """
        self.src = src
        self.dist = dist

    def read_files(self):
        """
        读取src目录下的所有文件
        """
        ls = os.listdir(self.src)
        print(ls)
        for l in ls:
            self.backup_file(l)

    def backup_file(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹名称
        :return: 
        """""
        # 1、 判断 dist 目录是否存在，如果不存在就创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的目录不存在，创建完成")
        # 2、 判断文件是否为我们要备份的文件

        # 拼接完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)

        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
        # 3、读取文件内容
            print("开始备份.....")
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist, \
                open(full_src_path, 'r', encoding='utf-8') as f_src:
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break
                    # 4、 把文件内容写入到新的文件中
                    f_dist.write(rest)
                f_dist.flush()
            print("备份完成.....")
        else:
            print("文件类型不符合备份要求，跳过...")

if __name__ == '__main__':
    # 当前代码的目录名称
    base_path = os.path.dirname(os.path.abspath(__file__))
    # 要备份的文件目录地址
    src_path = os.path.join(base_path, 'src')
    # 备份后的文件目录地址
    dist_path = os.path.join(base_path, 'dist')
    # 开始备份
    bak = FileBackup(src_path, dist_path)
    bak.read_files()