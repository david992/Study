
from socket import *


def handClient(connfd):
    data = connfd.recv(4096)
    #print(data)
    data_lines = data.splitlines()
    for line in data_lines:
        print(line.decode())
    try:
        f = open("E:\Study\WLBC\index.html")
    except IOError:
        response = "http/1.1 404 not found\r\n"
        response +="\r\n"
        response += "*********not found**********"
    else:
        response = "http/1.1 200 OK\r\n"
        response += "\r\n"
        response += f.read()
    finally:
        connfd.send(response.encode())
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8888))
    sockfd.listen(5)
    print("Listen to the port  8888")
    while True:
        connfd,addr=sockfd.accept()
        handClient(connfd)
        connfd.close()
if __name__ == "__main__":
    main()