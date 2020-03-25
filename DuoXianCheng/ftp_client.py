from socket import  *
import  os,sys,time,signal


#操作文件功能
class Ftp_client(object):
    def __init__(self,socket):
        self.socket = socket
    def do_quit(self):
        self.socket.send(b'Q')

    def do_list(self):
        self.socket.send(b"L") #发送请求
        #等待回复
        data = self.socket.recv(1024).decode()
        if data == "ok":
            data = self.socket.recv(4096).decode()
            files = data.split("#")
            for file in files:
                print(file)
            print("文件列表展示完毕")
        else:
            #有服务器返回失败原因
            print(data)
    def do_get(self,filename):
        self.socket.send(("G" + filename).encode())
        data = self.socket.recv(1024).decode()
        if data == "ok":
            fd = open (filename,"wb")
            while   True:
                data = self.socket.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
                fd.close()
                print(" %s 下载完成\n"%filename)
        else:
            print(data)
#网络连接
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("服务器连接错误",e)
        return
    ftp = Ftp_client(s)
    while True:
        print("==========命令==========")
        print("**********list*********")
        print("********get file*******")
        print("********put file*******")
        print("**********quit*********")
        print("========================")
        cmd = input("输入命令")
        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(" ")[-1]
            ftp.do_get(filename)
        elif cmd.strip() == "quit":
            ftp.do_quit()
            s.close()
            sys.exit("退出，谢谢使用")
        else:
            print("请输入正确命令")
            continue

if __name__ == "__main__":
    main()
