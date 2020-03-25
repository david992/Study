#客户端
import socket

#声明socket类型，同时生成socket连接对象
client = socket.socket()

#发起连接
client.connect(('127.0.0.1',8888))
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        print('quit')
        break
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print("Receive:",data.decode())
client.close()