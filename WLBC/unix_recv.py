from socket import *
import  os

sock_file ="./sock_file"
if os.path.exists(sock_file):
    os.remove(sock_file)

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.bind(sock_file)
sockfd.listen(5)

while True:
    c,addr=sockfd.accept()
    while True:
        data=c.recv(1024)
        if data:
            print(data.decode())
            c.send(b"Receive")
        else:
            break
        c.close()
    sockfd.close()
