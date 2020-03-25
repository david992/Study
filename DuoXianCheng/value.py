from multiprocessing import  Process,Value,freeze_support
import  time
import random

#创建共享进程
money = Value("i",2000)

#操作共享内存+
def depo():
    for i in range(100):
        time.sleep(0.05)
        #对value属性进行操作
        money.value +=random.randint(1,200)
#操作共享内存-
def draw():
    print("******")
    for i in range(100):
        time.sleep(0.04)
        money.value  -=random.randint(1,180)
def main():
    d = Process(target=depo)
    w = Process(target=draw)
    d.start()
    w.start()
    d.join()
    w.join()
    print("余额：",money.value)

if __name__ == '__main__':
    freeze_support()
    main()

