L = []
while True:
    s = input("输入：")
    if not s:
        break
    L.append(s)
print(L)
A="111,222,333,444,555,666"
B=A.split(",")
print(B)
print("*".join(B))
s=0
i = len(L) - 1
while i >= 0:
    print(L[i])
    s += len(L[i])
    i -= 1
print("个数：",s)

