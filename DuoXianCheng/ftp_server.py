from socket import  *
import  os,sys,time,signal
from multiprocessing import  Process,freeze_support

#文件库路径
file_path="E:\\Study\\venv\\"
host = "127.0.0.1"
port = 8888
ADDR = (host,port)

def  fun(s,c):
    print("子进程")
    s.close()
    ftp = FtpServer(c)
    while True:
        data = c.recv(1024).decode()
        if not data or data[0] == "Q":
            c.close()
            sys.exit("客户端退出")
        elif data[0] == "L":
            ftp.do_list(c)
        elif data [0] == "G":
            filename =data.split(" ")[-1]
            ftp.do_get(filename)


#文件服务器功能
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        print("*************")
        #获取文件列表
        file_list = os.listdir(file_path)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send("ok")
            time.sleep(0.1)
        for file in file_list:
            if file[0]  != "." and os.path.isfile(file_path+file):
                files = files + file + "#"
                self.connfd.sendall(files.encode())
    def fo_get(self,filename):
        try:
           fd =  open(file_path + filename,"rb")
        except:
            self.connfd.send("文件不存在".encode())
            return
        self.connfd.send(b"ok")
        time.sleep(0.1)
        #发送文件
        while True:
            data = fd.read(1024)
            if not  data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        print("发送完毕")

#创建套接字 接收客户端连接 创建进程
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #处理子进程退出
    # signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 8888...")

    while True:
        try:
            c,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as  e:
            print("服务器异常",e)
            continue
        print("已连接客户端",addr)
        #创建子进程
        # pid = os.fork()
        # if pid == 0:
        p = Process(target=fun,args=(s,c))
        #     s.close()
        #     ftp = FtpServer(c)
        #     while True:
        #         data = c.recv(1024).decode()
        #         if not data:
        #             c.close()
        #             sys.exit("客户端退出")
        #         elif data[0] == "L":
        #             ftp.do_list(c)
        print("主进程")
        # else:
        #     c.close()
        #     continue

if __name__ == "__main__":
    freeze_support()
    main()
