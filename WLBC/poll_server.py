from select import *
from socket import *
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#1.创建poll对象
p = select.poll()

#fileno————>IO对象字典
fdmap={s.fileno(),s}
#2.添加注册事件
p.register(s,select.POLLIN | select.POLLERR)

while True:
    events = p.poll()
    for fd,event in events:
        if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("connect from ",addr)
            #添加新的关注事件
            p.register(c,select.POLLIN |select.POLLHUP)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data= fdmap[fd].recv(1024)
            #客户端退出，从关注事件移出
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fromfd[fd]
            else:
                print(data.decode())
                fromfd[fd].send(b"Receive")