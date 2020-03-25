from socket import  *
import os,sys
import  multiprocessing as mp

def send_msg(s,name,addr):
    """
    发送消息
    :param s:
    :param name:
    :param addr:
    :return:
    """
    while True:
        text = input("发言>>")
        if text.strip()=="quit":
            msg ="Q "+name
            s.sendto(msg.encode(),addr)
            sys.exit("退出聊天室")
        msg = 'C  %s %s'%(name,text)
        s.sendto(msg.encode(),addr)

def recv_msg(s):
    while True:
        data,addr=s.recvfrom(2048)
        if data.decode()=="EXIT":
            sys.exit(0)
        print(data.decode()+"\n发言：",end="")

def main():
    """
    创建套接字，登录，，创建子进程
    :return:
    """
    #从命令行获取服务短地址
    # if len(sys.argv) < 3:
    #     print("argv is error")
    HOST = "127.0.0.1"
    PORT = 8888
    ADDR = (HOST,PORT)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("请输入姓名>>")
        msg = "L "+name
        #发送登录请求
        s.sendto(msg.encode(),ADDR)
        #等待服务器回复
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            #不成功则回复原因
            print(data.decode())
        #创建父子进程
        # pid = os.fork()
        # if pid < 0:
        #     sys.exit("创建子进程失败")
        # elif pid ==0 :
        #     send_msg(s,name,ADDR)
        # else:
        #     recv_msg(s)
        p = mp.Process(target=recv_msg, args=(s,))
        p.start()
        send_msg(s,name,ADDR)
        p.join()

if __name__ == "__main__":
    mp.freeze_support()

    main()
