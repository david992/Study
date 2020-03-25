i=int(input("请输入一个数："))
j=1
while j <= i:
    print(("*" * (2 * j - 1)).center((2 * i - 1)))
    j += 1
# for p in range(1,i+1):
#     Spece=i-p
#     print(" " * Spece + "*" * (2 * p - 1 ))

m=1
while m <= i:
    print("*".center(2 * i -1))
    m += 1
