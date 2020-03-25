#服务器端
from socket import *
#1.创建套接字 参数：socket_family：选择地址族类型
#                 socket_type：套接字类型 {流式 sock_stream 和数据报式 sock_dgram
#                 proto：选择子协议类型
sockfd = socket(AF_INET,SOCK_STREAM,proto = 0)

#2.绑定服务器地址 绑定IP地址 参数：元组（ip，port）
sockfd.bind(("localhost",8888))

#3.设置监听套接字 参数：监听队列大小
sockfd.listen(5 )

#4.等待处理客户端连接请求 参数： connfd:客户端连接套接字  addr：连接的客户端地址
while True  :
    print("等待连接......")
    connfd,addr=sockfd.accept()
    print("连接自",addr)
    # 5.消息接收
    # 接受对应客户端消息 参数：buffersize为一次接受多少字节   返回接收的内容
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        #发送给对应客户端  参数：要发送的内容，必须是bytes格式   返回实际发送消息的大小
        n=connfd.send(b'receive your message')
        print("发送了%d个字节"%n)
#6.关闭套接字
    connfd.close()
sockfd.close()