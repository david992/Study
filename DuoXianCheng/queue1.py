from multiprocessing import Queue,Process,freeze_support
from time import sleep

# 创建消息队列
q = Queue(1)


def fun1():
    sleep(1)
    q.put(1)
    print(q.full())

def fun2():
    sleep(2)
    print("收到消息",q.get(False))
    print(q.empty())

def main():

    p1 = Process(target=fun1)
    p2 = Process(target=fun2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    freeze_support()
    main()
