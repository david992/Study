import  signal,time
signal.alarm(5)

#默认方式
# signal.signal(signal.SIGALRM,signal.SIG_DFL)

#忽略信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.signal(signal.SIG_IGN,signal.SIG_IGN)
while True:
    time.sleep(2)
    print("wait")