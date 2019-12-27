import time
import sys
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from db_fixture import test_data


sys.path.append('./interface')
sys.path.append('./db_fixture')
# 定义测试用例集
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='testcase_*.py')

if __name__ == "__main__":
    # 初始化接口测试数据
    test_data.init_data()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='领导干部个人有关事项（Java版）接口自动化测试报告',
                            description='MySQL数据库,requests包实现')
    runner.run(testsuit)
    fp.close()
