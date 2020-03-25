#!/usr/bin/env python3
#UDP客户端

from  socket import *
import sys
if len(sys.argv)<3:
    print("argv is error!")
#1.创建套接字
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
sockfd =socket(AF_INET,SOCK_DGRAM)

#2.收发消息
while True:
    data = input("消息：")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print("从服务器收到：",data.decode())
#3.退出
sockfd.close()