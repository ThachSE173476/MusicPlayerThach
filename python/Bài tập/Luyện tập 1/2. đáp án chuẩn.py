# thứ tự nhận đề của alice pos = 2*(p-1)+q
# đề alice nhận pos%k
# muốn nhận cùng để phải ngồi cách nhau k vị trí
# vị trí bob cần ngồi pos - k
n = int(input())
k = int(input())
p = int(input())
q = int(input())
thu_tu_nhan_de_cua_alice = 2*(p-1)+q
if thu_tu_nhan_de_cua_alice <= k:
    thu_tu_nhan_de_cua_bob = thu_tu_nhan_de_cua_alice + k
else:
    thu_tu_nhan_de_cua_bob = thu_tu_nhan_de_cua_alice - k
if thu_tu_nhan_de_cua_bob % 2 == 0:
    u = thu_tu_nhan_de_cua_bob//2
    v = 2
else: 
    u = thu_tu_nhan_de_cua_bob //2+1
    v =1
if thu_tu_nhan_de_cua_bob > n:
    print(-1)
else:
    print(u,v)