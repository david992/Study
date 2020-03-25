from greenlet import greenlet

def t1():
    print("11111")
    g2.switch()
    print("22222")
    g2.switch()


def t2():
    print("33333")
    g1.switch()
    print("44444")


g1 = greenlet(t1)
g2 = greenlet(t2)

g1.switch()