from Object.mysqlpython import Mysqlpython

sql = Mysqlpython("studb")
sql.zhixing("update sheng set id=999 where id=20;")
data=sql.all("select * from sheng where id =%s;",[1])
print(data)