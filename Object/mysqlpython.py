from pymysql import  *

class Mysqlpython:
    def __init__(self,database,
                 charset="utf8",
                 host="localhost",
                 user="root",
                 password="123456",
                 port=3306):
        self.database=database
        self.charset=charset
        self.host=host
        self.user=user
        self.password=password
        self.port=port
    def open (self):
        self.db = connect(host=self.host,user=self.user,
                                  password=self.password,
                                  port=self.port,
                                  database=self.database,
                                  charset=self.charset)
        self.cur=self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            print("执行成功")
        except Exception as e:
            self.db.rollback()
            print("执行失败",e)
        self.close()
    def all(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("查询失败",e)
        self.close()