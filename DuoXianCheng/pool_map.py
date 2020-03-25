from  multiprocessing import Pool
from  time import  sleep ,ctime

def worker(n):
    sleep(1)
    print("执行map事件")
    return n * n
if __name__ == '__main__':
    #创建进程池
    pool = Pool(processes=4)
    r = pool.map(worker,range(10))
    pool.close()
    pool.join()
    print(r)
