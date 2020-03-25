#UDP服务器端
from  socket import  *
#1.创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#2.绑定地址
sockfd.bind(("0.0.0.0",9999))

#3.消息收发  参数 data：接收的数据   addr：消息发送端的地址   返回值为发送的字节数
while True:
    data,addr=sockfd.recvfrom(1024)
    print("receive from %s：%s" %(addr,data.decode()))
    sockfd.sendto("收到你的消息".encode(),addr)
#4.关闭套接字
sockfd.close()