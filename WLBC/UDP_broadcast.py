from socket import *

#创建套接字
s =socket(AF_INET,SOCK_DGRAM)

#设置套接字可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#绑定端口
s.bind(("localhost",9999))

while True:
    try:
        msg,addr=s.recvfrom(1024)
        print("从{}中获取信息：{}".format(addr,msg.decode()) )
    except (KeyboardInterrupt,SyntaxError):
        raise
    except Exception as  e:
        print(e)
#关闭套接字
s.close()
