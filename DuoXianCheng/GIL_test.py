from DuoXianCheng.GIL import *
import threading,time
from multiprocessing import  Process
def io():
    write()
    read()
if __name__ == '__main__':
    counts = []
    t = time.time()
    for i in range(10):
        p = Process(target=io)
        counts.append(p)
        p.start()
    for i in counts:
        i.join()
    print("CPU", time.time() - t)