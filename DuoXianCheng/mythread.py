from  threading import  Thread
from time import  ctime,sleep

class MyThread():
    def __init__(self,target,name="666",args=(),kwargs={}):
        super().__init__()
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)

def player(song,sec):
    for i in range(5):
        print("pplaying {}:{}".format(song,ctime()))
        sleep(sec)
t = Thread(target=player,args=("666",),kwargs={"sec":2})
t.start()
t.join()