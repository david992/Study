from  socket import  *

sock_file="./sock_file"

sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.connect(sock_file)

while True:
    msg=input(">>")
    if msg:
        sockfd.send(msg.encode())
        print(sockfd.recv(1024).decode())
    else:
        break
    sockfd.close()