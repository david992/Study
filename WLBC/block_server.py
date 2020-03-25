from  socket import  *
from  time import  sleep,ctime

s = socket()
s.bind(("127.0.0.1",8888))
s.listen(3)
#将套接字设置为非阻塞
s.setblocking(0)

while True:
    print("Waiting for connect...")
    try:
        c,addr=s.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue
    else:
        print("connect from %s" %str(addr))
        while True:
            c.setblocking(1)   #是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
                               #[WinError 10035] 无法立即完成一个非阻止性套接字操作。
            data= c.recv(1024).decode()
            if not  data:
                break
            print(data)
            c.send(ctime().encode())
        c.close()
s.close()

