from datetime import datetime

from test004.utils.trans import tools as trans_tools
import test004.utils.work

def test_trans_tool():
    """测试 trans 包下的 tools 模块"""
    id1 = trans_tools.gen_trans_id()
    print(id1)
    date = datetime(2020, 5, 10, 21, 19, 30)
    id2 = trans_tools.gen_trans_id(date)
    print(id2)

def test_work_tool():
    """测试 work 模块"""
    file_name = 'C:/Users\wshap/Desktop/test.xlsx'
    res = test004.utils.work.tools.get_file_type(file_name)
    print(res)


if __name__ == '__main__':
    test_trans_tool()
    test_work_tool()
