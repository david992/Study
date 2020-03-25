from  multiprocessing import Pool
from  time import  sleep ,ctime

def worker(msg):
    sleep(1)
    print(msg)
    return ctime()
if __name__ == '__main__':
    #创建进程池
    pool = Pool(processes=4)
    result = []
    for i in range(10):
        msg = "hello %d"%i
        #将事件放入进程池队列
        r = pool.apply_async(worker,(msg,))
        result.append(r)
    pool.close()
    pool.join()
    for s in result:
        print(s.get()) #获取时间函数返回值
