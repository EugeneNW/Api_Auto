import sys
import time

sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-100000))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+10000))

# 创建数据
datas = {

}


def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
