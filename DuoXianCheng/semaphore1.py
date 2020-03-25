from multiprocessing import Semaphore,Process,freeze_support
import os
from time import sleep

sem = Semaphore(3)
def fun():
    print("进程%d等待信号量1" % os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("进程%d等待信号量2" % os.getpid())
    sleep(3)
    sem.release()
    print("进程%d等待信号量3" % os.getpid())

if __name__ == '__main__':
    freeze_support()
    jobs= []
    for i in range(4):
        p = Process(target=fun)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
    print(sem.get_value())
