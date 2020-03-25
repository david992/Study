import  gevent
from  gevent import monkey
monkey.patch_all()
from socket import  *
from  time import  ctime

def server(port):
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(("0.0.0.0",port))
    s.listen(5)

    while True:
        c,addr = s.accept()
        print("connect from ",addr)
        #handler(c) 普通魂环服务器
        gevent.spawn(handler,c) #协程服务器

def handler(c):
    while True:
        data = c. recv(1024)
        if not data :
            break
        print(data.decode())
        c.send(ctime().encode())
    c.close()
if __name__ == "__main__":
    server(8888)