import os

pid = os.fork()

if pid < 0 :
    print("创建失败")
elif pid == 0:
    #创建二级子进程
    p = os.fork()
    if p == 0 :
        pass #该做的事
    else:
        os._exit(0)
else:
    os.wait() #等待一级子进程退出
    pass #该做的事