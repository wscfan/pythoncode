import os
import os.path

class FileBackup(object):
    """
    文本文件备份
    """
    def __init__(self, src, dist):
        """
        构造方法
        :param src: 目录 需要备份的文件目录
        :param dist: 目录 备份后的目录
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
            self.backup_file2(l)

    def backup_file(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹名称
        """
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的目录不存在，创建完成。")
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == ".txt":
            with open(full_dist_path, 'w', encoding="utf-8") as f_dist:
                print(">>>开始备份【{0}】".format(file_name))
                with open(full_src_path, 'r', encoding="utf-8") as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                            break
                        f_dist.write(rest)
                    f_dist.flush()
                print("<<<备份完成【{0}】".format(file_name))
        else:
            print("文件类型不符合要求。")

    def backup_file2(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹名称
        """
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的目录不存在，创建完成。")
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == ".txt":
            with open(full_dist_path, 'w', encoding="utf-8") as f_dist,\
                open(full_src_path, 'r', encoding="utf-8") as f_src:
                print(">>>开始备份【{0}】".format(file_name))
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break
                    f_dist.write(rest)
                f_dist.flush()
            print("<<<备份完成【{0}】".format(file_name))
        else:
            print("文件类型不符合要求。")

if __name__ == '__main__':
    # # 要备份的文件目录地址
    # src_path = 'C:\\mycode\pythoncode\\test003\\module2\\src'
    # # 备份后的文件目录地址
    # dist_path = 'C:\\mycode\pythoncode\\test003\\module2\\dist'

    # 要备份的文件目录地址
    base_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_path, 'src')
    print(src_path)
    # 备份后的文件目录地址
    dist_path = os.path.join(base_path, 'dist')
    bak = FileBackup(src_path, dist_path)
    bak.read_files()