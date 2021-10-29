n = int(input())
phan_so = []
for i in range(n):
    phan_so.append(list(map(int,input().split())))
import math
for i in range(n):
    tu = phan_so[i][0] //(math.gcd(phan_so[i][0],phan_so[i][1]))
    mau = phan_so[i][1] //(math.gcd(phan_so[i][0],phan_so[i][1]))
    if mau ==1:
        print(tu)
    else:
        print(tu,mau)

