from multiprocessing import Process
import os
from signal import *
from time import  sleep

def sal_handler(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print("到站下车")
        os._exit()

def driver_handler(sig,frame):
    if sig == SIGUSR1:
        print("老司机，发车！")
    elif sig == SIGUSR2:
        print("车速过快 ")
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)

#子进程代表售票员
def saler():
    signal(SIGINT,sal_handler)
    signal(SIGQUIT,sal_handler)
    signal(SIGUSR1,sal_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        sleep(1)
        print("好好学习")

if __name__ == '__main__':

    p = Process(target=saler)
    p.start()
    #父进程
    signal(SIGINT, SIG_IGN)
    signal(SIGQUIT, SIG_IGN)
    signal(SIGUSR1,driver_handler)
    signal(SIGUSR2,driver_handler)
    signal(SIGTSTP,driver_handler)
    p.join()