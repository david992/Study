from socket import  *
from time import  sleep

#设置目标地址
dest = ("127.0.0.1",9999)

#创建套接字
s= socket(AF_INET,SOCK_DGRAM)

#设置发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    sleep(2)
    s.sendto("welcome!".encode(),dest)

s.close()
