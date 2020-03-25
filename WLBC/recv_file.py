#作为服务器端
from socket import  *

s = socket()

s.bind(("127.0.0.1",8888))
s.listen(3)
c,addr = s.accept()
print("已连接%s" %str(addr))

f = open("recv.jpg" ,"wb")

while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()