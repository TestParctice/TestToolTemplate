# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/5 16:26
@Author:yzx
"""

import pymysql


class DB:
    def __init__(self, host, user, passwd):
        self.conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db='')
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))


if __name__ == '__main__':
    db = DB(host="106.14.227.119", user="root", passwd="root")
    res = db.query("select * from api.apirecord;")
    print(res)
