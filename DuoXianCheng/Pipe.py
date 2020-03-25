from multiprocessing import  Process , Pipe
import  time ,os

fd1,fd2 = Pipe(True)
def fun(name):
    time.sleep(1)
    #管道中写入内容
    fd1.send("hello"+ str(name))
    # print(name)
if __name__ == '__main__':
    jobs = []
    for i in range(5):
        P = Process(target=fun,args=(i,))
        jobs.append(P)
        P.start()
    for i in range(5):
        #读取管道内容
        data = fd2.recv()
        print(data)
    for i in jobs:
        i.join()