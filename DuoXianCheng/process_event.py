from multiprocessing import  Event,Process
from  time import  sleep

e = Event()
def wait_event():
    print("想操作临界区")
    e.wait()
    print("开始操作",e.is_set())
    with open("file") as f :
        print(f.read())

def wait_event_timeout():
    print("也想操作临界区")
    e.wait(2)
    if e.is_set():
        with open ("file") as f:
            print(f.read())
    else:
        print("无法读取文件")
if __name__ == '__main__':
    p1 = Process(target=wait_event)
    p1.start()
    p2 = Process(target=wait_event_timeout)
    p2.start()
    print("主进程操作")
    with open ("file","w") as f:
        sleep(3)
        f.write("hello word")
    e.set()
    print("释放临界区")
    p1.join()
    p2.join()