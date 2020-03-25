import  threading
import os
from time import  sleep

#线程函数
def music():
    for i in range(10):
        sleep(0.5)
        print("music")

t = threading.Thread(target=music)
t.start()
for i in range(5):
    sleep(1)
    print("music000")
t.join()