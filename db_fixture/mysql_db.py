# coding=utf8
import pymysql.cursors
import configparser
from os.path import abspath, dirname

base_dir = dirname(dirname(abspath(__file__)))
file_path = base_dir.replace('\\', '/') + "/db_config.ini"

# 读取db_config配置
cf = configparser.ConfigParser()
cf.read(file_path)
host = cf.get("mysql_config", "host")
port = cf.get("mysql_config", "port")
db = cf.get("mysql_config", "db_name")
user = cf.get("mysql_config", "user")
password = cf.get("mysql_config", "password")


class DB:
    def __init__(self):
        try:
            # MySQL数据库连接
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # 插入数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        # print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    # 关闭数据库
    def close(self):
        self.connection.close()

    # 数据初始化
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    table_name = "table_name"
    data = {}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
