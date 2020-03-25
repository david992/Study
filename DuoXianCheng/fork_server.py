from socket import  *
import os, sys
import signal

def client_handler(c):
    print("处理子进程请求：", c.getpeername())
    try:
        while True:
            data = c.recv(1024)
            if not data :
                break
            print(data)
            c.send("收到客户的请求".encode())
    except (KeyboardInterrupt,SystemError):
        sys.exit("客户端退出！")
    except Exception as e:
        print("Error:",e)
    c.close()

HOST = ""
PORT = 8888
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind()
s.listen(5)

print("进程 %d等待客户端连接"%os.getpid())
#在父进程忽略子进程状态状态 子进程退出时系统自动处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("错误：",e)
        continue
    #为客户端创建新的进程处理请求
    pid = os.fork()
    if pid == 0:
        s.close()
        client_handler(c)
    else:
        c.close()
        continue