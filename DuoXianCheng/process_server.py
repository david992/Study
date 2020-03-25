from socket import *
import os,sys
import  multiprocessing as mp


def do_chat(s,user,name,text):
    """
    聊天功能
    :param s:
    :param user:
    :param name:
    :param text:
    :return:
    """
    msg ="\n%s 说：%s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_login(s,user,name,addr):
    """
    登录功能
    :return:
    """
    if (name in user) or name == "管理员":
        s.sendto("用户已存在".encode(),addr)
        return
    s.sendto(b"OK",addr)
    #通知其他人
    msg = "\n欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #添加用户
    user[name]=addr

def do_quit(s,user,name):
    """
    退出聊天室
    :param s:
    :param user:
    :param name:
    :return:
    """
    msg= "\n"+name + "退出聊天室"
    for i in user:
        if i == name:
            s.sendto(b"EXIT",user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]

def do_parent(s):
    """
    接收客户端请求
    :return:
    """
    user={} #存储结构 {"zhangsan"：("127.0.0.1",9999)}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(" ")
        #判断请求类别
        if msgList[0] == "L":
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == "C":
            do_chat(s,user,msgList[1]," ".join(msgList[2:]))
        elif msgList[0] == "Q":
            do_quit(s,user,msgList[1])
def do_child(s,addr):
    """"
    做管理员喊话
    :return:
    """
    while True:
        msg = input("管理员消息:")
        msg = "C 管理员"+msg
        s.sendto(msg.encode(),addr)

def main():
    """
    创建网络 创建进程 调用函数
    :return:
    """
    #server address
    ADDR = ("0.0.0.0",8888)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    #创建单独进程处理管理员喊话功能
    # pid = os.fork()
    # if pid < 0:
    #     sys.exit("创建进程失败")
    # elif pid == 0:
    #     do_child()
    # else:
    #     do_parent(s)

    p = mp.Process(target=do_parent,args=(s,))
    p.start()
    do_child(s,addr=ADDR)
    print("*******")
    p.join()

if __name__ == "__main__":
    # mp.freeze_support()
    main()