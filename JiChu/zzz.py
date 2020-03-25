L=[3,5]
L[:]=[11,22,13,40,55,46]
L.insert(0,0)
L.insert(7,1)
L.append(666)
print (L)
# L[:]=L[::-1]
# del L[len(L)-1]
# print(L)
print(L.index(666))
print(L.index(13,3))
print(L.count(46))   #计数
L.reverse()
print(L)
L.sort(reverse=True)
print(L)