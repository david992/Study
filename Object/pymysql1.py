import pymysql

# 创建与数据库连接对象
db = pymysql.connect(host="localhost",user='root',password="123456",
                     database="studb",charset="utf8")

# 利用db方法创建游标对象
cur = db.cursor()

#利用游标对象的excute（）方法执行命令
s_id = input("请输入id：")
s_name = input("请输入省份：")
try:
    sql_insert = "insert into sheng (s_id,s_name) " \
                 "values(%s,%s);"
    cur.execute(sql_insert,[s_id,s_name])
    print("添加成功！")
    db.commit()
except Exception as e:
    print("Failed",e)
    db.rollback()
#提交到数据库执行
# db.commit()

#关闭游标对象
cur.close()

#关闭数据库连接
db.close()