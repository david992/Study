from select import select
from socket import *

s = socket(AF_INET,SOCK_STREAM,0)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = []

#提交检测我们关注的io等待io发生
while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr=r.accept()
            print("connect from %s" %str(addr))
            rlist.append(c)  #添加到关注列表
        else:
            data = r.recv(1024)
            if not data :
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                #将客户端套接字放入wlist
                wlist.append(r)
                # r.send(b'receive your message')

    for w in ws:
        w.send(b'Receive your message')
        wlist.remove(w)

    for x in xs:
        if x is s :
            s.close()
