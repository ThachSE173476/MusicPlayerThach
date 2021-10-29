q = int(input())
import math
lan_lap = 0
while lan_lap < q:
    n = int(input())
    danh_sach = list(map(int,input().split()))
    lan_lap +=1
    tong = sum(danh_sach)
    print(math.ceil(tong/n))