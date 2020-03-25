from multiprocessing import Process
import  time

class ColckProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    #重写run
    def run(self):
        for i in range(5):
            print("The time is {}".format(time.ctime()))
            time.sleep(self.value)

if __name__ == '__main__':
    p = ColckProcess(2)
    p.start()
    p.join()