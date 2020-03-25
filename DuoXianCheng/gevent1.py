import gevent

def foo(a,b):
    print("a = %d, b = %d"%(a,b))
    gevent.sleep(2)
    print("running foo again")

def bra():
    print("running bra")
    gevent.sleep(1)
    print("running bra again")

f = gevent.spawn(foo,1,2)
g = gevent.spawn(bra)

gevent.joinall([f,g])