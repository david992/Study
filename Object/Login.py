from Object.mysqlpython import Mysqlpython
from hashlib import sha1
#sha1加密

uname = input("请输入用户名：")
pwd = input("请输入密码：")

s1 = sha1() #创建加密对象
s1.update(pwd.encode("utf8"))  #指定编码
pwd2 = s1.hexdigest()   #返回16进制加密结果

sqlh = Mysqlpython("studb")
select = "select password from user where  \
         username= %s;"
result = sqlh.all(select,[uname])
if len(result) == 0:
    print("用户不存在")
elif result[0][0] == pwd2:
    print("登录成功")
else:
    print("密码错误")